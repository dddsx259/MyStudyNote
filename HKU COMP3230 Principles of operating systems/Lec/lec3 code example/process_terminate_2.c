#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    
    // Fork the process
    pid_t pid = fork();

    if (pid == 0) {
        exit(-1);
    }

    while (1) {}

    return 0;
}