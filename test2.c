#include <stdlib.h>
#include <stdio.h>

#define TRUE 1
#define FALSE 0

// This is the first CTF challenge! I fuzzed it and it did indeed show a security vulnerability

int printName();

int main(int argv, char **argc) {

    printf("Welcome!\n");
    printName();
    printf("Everything is good.\n");

    return EXIT_SUCCESS;
}

int printName() {
    int isAdmin = FALSE;
    char name[16];

    printf("What is your name?\n");
    printf("> ");
    gets(&name);

    if (isAdmin == FALSE) {
        printf("Welcome, %s!\n", name);
        printf("You are in this program, but we do not grant you the rank of Admin.\n");
        printf("Now go away, or I will taunt you a second time.\n");
    } else {
        printf("Welcome, %s!\n", name);
        printf("With great power comes great responsibility...\n");
    }
    return EXIT_SUCCESS;
}
