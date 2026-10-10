CC      = gcc
CFLAGS  = -O0

.PHONY: all clean

all: check_syscall.s

check_syscall.s: check_syscall.c
	$(CC) -S -O0 -o $@ $<

clean:
	rm -f check_syscall.s
