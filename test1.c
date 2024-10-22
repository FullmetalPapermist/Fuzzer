#include <stdio.h>

int main(void) {
    char name[1];
    gets(name, stdin);
    printf("Hello, %s", name);

    return 0;
}