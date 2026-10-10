CC      = gcc
CFLAGS  = -Wall -Wextra -g
SRCS    = $(wildcard *.c)
BINS    = $(SRCS:.c=)

.PHONY: all clean

all: $(BINS)

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(BINS)
