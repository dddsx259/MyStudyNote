#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

enum {
    DEFAULT_LOOPS = 100000,
    MAX_LOOPS = 100000000
};

int counter = 0;
int loops = DEFAULT_LOOPS;
pthread_mutex_t counter_mutex = PTHREAD_MUTEX_INITIALIZER;

static void print_usage(const char *program)
{
    fprintf(stderr, "Usage: %s [loops]\n", program);
    fprintf(stderr, "Default: loops=%d\n", DEFAULT_LOOPS);
}

static int parse_positive_int(const char *text, const char *name, int *value)
{
    char *end = NULL;
    long parsed;

    errno = 0;
    parsed = strtol(text, &end, 10);
    if (errno == ERANGE || end == text || *end != '\0' ||
        parsed < 1 || parsed > MAX_LOOPS) {
        fprintf(stderr, "Invalid %s: %s (must be 1..%d)\n",
                name, text, MAX_LOOPS);
        return -1;
    }

    *value = (int)parsed;
    return 0;
}

static void *worker(void *arg)
{
    (void)arg;

    for (int i = 0; i < loops; ++i) {
        counter++;
    }

    return NULL;
}

int main(int argc, char *argv[])
{
    pthread_t p1;
    pthread_t p2;
    int join_failed = 0;

    if (argc > 2) {
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }
    if (argc == 2 && parse_positive_int(argv[1], "loops", &loops) != 0) {
        return EXIT_FAILURE;
    }

    printf("Initial value : %d\n", counter);

    pthread_create(&p1, NULL, worker, NULL);
    pthread_create(&p2, NULL, worker, NULL);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);

    printf("Final value   : %d\n", counter);
    printf("Expected value: %d\n", 2 * loops);
    return counter == 2 * loops ? EXIT_SUCCESS : EXIT_FAILURE;
}
