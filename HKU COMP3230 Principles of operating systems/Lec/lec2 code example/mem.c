#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

enum {
    DEFAULT_ROUNDS = 5,
    MAX_ROUNDS = 1000000
};

static void print_usage(const char *program)
{
    fprintf(stderr, "Usage: %s [initial-value] [rounds]\n", program);
    fprintf(stderr, "Defaults: initial-value=0, rounds=%d\n", DEFAULT_ROUNDS);
}

static int parse_int(const char *text, const char *name, int *value)
{
    char *end = NULL;
    long parsed;

    errno = 0;
    parsed = strtol(text, &end, 10);
    if (errno == ERANGE || end == text || *end != '\0' ||
        parsed < INT_MIN || parsed > INT_MAX) {
        fprintf(stderr, "Invalid %s: %s\n", name, text);
        return -1;
    }

    *value = (int)parsed;
    return 0;
}

static int parse_positive_int(const char *text, const char *name, int *value)
{
    char *end = NULL;
    long parsed;

    errno = 0;
    parsed = strtol(text, &end, 10);
    if (errno == ERANGE || end == text || *end != '\0' ||
        parsed < 1 || parsed > MAX_ROUNDS) {
        fprintf(stderr, "Invalid %s: %s (must be 1..%d)\n",
                name, text, MAX_ROUNDS);
        return -1;
    }

    *value = (int)parsed;
    return 0;
}

/* The book's Spin(1), written locally so this file has no hidden dependency. */
static void spin_for_one_second(void)
{
    struct timespec start;
    struct timespec now;

    if (clock_gettime(CLOCK_MONOTONIC, &start) == -1) {
        perror("clock_gettime");
        exit(EXIT_FAILURE);
    }

    for (;;) {
        double elapsed;

        if (clock_gettime(CLOCK_MONOTONIC, &now) == -1) {
            perror("clock_gettime");
            exit(EXIT_FAILURE);
        }

        elapsed = (double)(now.tv_sec - start.tv_sec) +
                  (double)(now.tv_nsec - start.tv_nsec) / 1000000000.0;
        if (elapsed >= 1.0) {
            return;
        }
    }
}

int main(int argc, char *argv[])
{
    int initial_value = 0;
    int rounds = DEFAULT_ROUNDS;
    int *p;

    if (argc > 3) {
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    if (argc >= 2 && parse_int(argv[1], "initial-value", &initial_value) != 0) {
        return EXIT_FAILURE;
    }
    if (argc == 3 && parse_positive_int(argv[2], "rounds", &rounds) != 0) {
        return EXIT_FAILURE;
    }

    p = malloc(sizeof(*p));

    *p = initial_value;
    printf("(%ld) memory address of p: %p\n", (long)getpid(), (void *)p);
    fflush(stdout);

    for (int i = 0; i < rounds; ++i) {
        spin_for_one_second();
        (*p)++;
        printf("(%ld) p: %d\n", (long)getpid(), *p);
        fflush(stdout);
    }

    free(p);
    return EXIT_SUCCESS;
}
