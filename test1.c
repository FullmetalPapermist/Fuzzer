#include <stdio.h>

int main(void) {
    printf("working\n");
    char name[1];
    gets(name, stdin);
    printf("Hello, %s", name);

    return 0;
}