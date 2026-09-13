#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static void print_usage(const char *program)
{
    fprintf(stderr, "Usage: %s [path]\n", program);
    fprintf(stderr, "Default path: ./io_demo_output.txt\n");
}

static int write_all(int file_descriptor, const char *data, size_t length)
{
    size_t written = 0;

    while (written < length) {
        ssize_t result = write(file_descriptor, data + written, length - written);

        if (result < 0) {
            if (errno == EINTR) {
                continue;
            }
            return -1;
        }
        if (result == 0) {
            errno = EIO;
            return -1;
        }

        written += (size_t)result;
    }

    return 0;
}

int main(int argc, char *argv[])
{
    const char *path = "io_demo_output.txt";
    const char message[] = "hello world\n";
    const size_t message_length = sizeof(message) - 1;
    int file_descriptor;

    if (argc > 2) {
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }
    if (argc == 2) {
        path = argv[1];
    }

    file_descriptor = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);

    write_all(file_descriptor, message, message_length);

    close(file_descriptor);

    printf("Wrote %zu bytes to %s\n", message_length, path);
    return EXIT_SUCCESS;
}
