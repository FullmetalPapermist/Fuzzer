#include <stdio.h>

// Dangerous format string usage!

int main() {
   char buffer[50];

   printf("Enter a string: ");
   if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
       printf(buffer);
   } else {
       printf("Error reading input.");
   }

   return 0;
}