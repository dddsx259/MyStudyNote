#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int c = 100;

int main() {
    
    // Fork the process
    pid_t pid = fork();

    if (c == 100) {
        printf("X\n");
    }
    

    // terminate the processes properly
    if (pid != 0) {
        int status;
        waitpid(pid, &status, 0);
    }

    return 0;
}