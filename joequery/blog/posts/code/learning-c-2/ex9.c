#include <stdio.h>
int main(){
    // On my computer, this prints 32 and 64. It may be different on your
    // computer!
    printf("sizeof unsigned int: %zu\n", sizeof(unsigned int)*8);
    printf("sizeof long: %zu\n", sizeof(long)*8);


    // Note that long/short, when by themselves, act as shorthand for
    // "long int" and "short int" respectively.
    printf("sizeof long int: %zu\n", sizeof(long int)*8);

    if(-1L < 1U){
        printf("-1 < 1. Duh!\n");
    }
    else{
        printf("-1 > 1?! WTF?!\n");
    }

    if(-1L < 1UL){
        printf("-1 < 1. Duh!\n");
    }
    else{
        printf("-1 > 1?! WTF?!\n");
    }

    return 0;
}
