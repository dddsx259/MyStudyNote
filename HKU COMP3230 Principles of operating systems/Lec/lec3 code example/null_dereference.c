#include <stdio.h>

int main() {

    printf("I am going to trigger SIGSEV\n");
    int *ptr = NULL;
    *ptr = 42; // Trigger SIGSEGV

    return 0;
}