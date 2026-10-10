#include <fcntl.h>

void test_open() {
    int fd = open("test.txt", O_RDONLY);
}

int main() {
    test_open();
    return 0;
}