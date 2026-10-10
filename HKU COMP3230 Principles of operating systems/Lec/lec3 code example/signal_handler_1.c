#include <stdio.h>
#include <signal.h>
#include <setjmp.h>

void handle_segv(int sig) {
    printf("Caught SIGSEGV: %d, but I don't want to die T_T\n", sig);
    return;
}

int main() {
    signal(SIGSEGV, handle_segv); // Quick signal registration

    printf("I am going to trigger SIGSEV\n");
    int *ptr = NULL;
    *ptr = 42; // Trigger SIGSEGV

    return 0;
}