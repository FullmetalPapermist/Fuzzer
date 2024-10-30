#include <stdio.h>
#include <string.h>

int main() {
    char buffer[50];

    printf("Enter a string: ");
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        if (strcmp(buffer, "a") == 0) {
            printf("ERROR!\n");
            return 1;
        }
        printf("You entered: %s", buffer);
    } else {
        printf("Error reading input.");
    }

   return 0;
}