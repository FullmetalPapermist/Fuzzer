#include <stdio.h>

// Standard buffer overflow - using an array of 1 to quickly cause a buffer overflow with brute force

int main(void) {
    printf("working\n");
    char name[1];
    gets(name, stdin);
    printf("Hello, %s", name);

    return 0;
}