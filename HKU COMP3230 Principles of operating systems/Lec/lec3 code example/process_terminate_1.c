#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    
    // Fork the process
    pid_t pid = fork();

    if (pid == 0) {
        while (1) {}
    }

    // terminate the processes properly
    if (pid != 0) {
        int status;
        waitpid(pid, &status, 0);
    }

    return 0;
}