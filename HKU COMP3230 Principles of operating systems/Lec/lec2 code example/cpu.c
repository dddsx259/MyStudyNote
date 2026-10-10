#define _GNU_SOURCE
#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <sched.h>
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
    fprintf(stderr, "Usage: %s [message] [rounds]\n", program);
    fprintf(stderr, "Defaults: message=A, rounds=%d\n", DEFAULT_ROUNDS);
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
    const char *message = "A";
    int rounds = DEFAULT_ROUNDS;

    if (argc > 3) {
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    if (argc >= 2) {
        message = argv[1];
    }
    if (argc == 3 && parse_positive_int(argv[2], "rounds", &rounds) != 0) {
        return EXIT_FAILURE;
    }

    for (int i = 0; i < rounds; ++i) {
        int current_cpu;

        spin_for_one_second();
        current_cpu = sched_getcpu();

        printf("(%ld) [CPU %d] p: %s\n", (long)getpid(), current_cpu, message);
        fflush(stdout);
    }

    return EXIT_SUCCESS;
}
