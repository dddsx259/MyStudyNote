#include <stdio.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf env;

void handle_segv(int sig) {
    printf("Caught SIGSEGV: %d, but I don't want to die T_T\n", sig);
    siglongjmp(env, 1); // Jump directly out of the faulting instruction
    return;
}

int main() {
    signal(SIGSEGV, handle_segv); // Quick signal registration

    if (sigsetjmp(env, 1) == 0) {
        printf("I am going to trigger SIGSEV\n");
        int *ptr = NULL;
        *ptr = 42; // Trigger SIGSEGV
    } else {
        printf("Recovered safely!\n");
    }

    printf("Program finished normally.\n");
    return 0;
}