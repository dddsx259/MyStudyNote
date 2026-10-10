CC = gcc
CFLAGS = -std=c11 -O0
THREAD_FLAGS = -pthread
PROGRAMS = cpu mem threads threads_mutex io

.PHONY: all clean

all: $(PROGRAMS)

cpu: cpu.c
	$(CC) $(CFLAGS) $< -o $@ # gcc -std=c11 -O0 cpu.c -o cpu

mem: mem.c
	$(CC) $(CFLAGS) $< -o $@ # gcc -std=c11 -O0 mem.c -o mem

threads: threads.c
	$(CC) $(CFLAGS) $(THREAD_FLAGS) $< -o $@ # gcc -std=c11 -pthread -O0 threads.c -o threads

threads_mutex: threads_mutex.c
	$(CC) $(CFLAGS) $(THREAD_FLAGS) $< -o $@ # gcc -std=c11 -pthread -O0 threads_mutex.c -o threads_mutex

io: io.c
	$(CC) $(CFLAGS) $< -o $@ # gcc -std=c11 -O0 io.c -o io

clean:
	rm -f $(PROGRAMS)
