#include <stdio.h>
int main(){
    short int x = 10;
    // int can actually be omitted here
    short y = 10;

    // zu is size_t type specifier
    printf("%zu\n", sizeof x);
    printf("%zu\n", sizeof y);

    long int lx = 10;
    long ly = 10;

    printf("%zu\n", sizeof lx);
    printf("%zu\n", sizeof ly);
    return 0;
}
