#include <stdio.h>
#include <limits.h>

// This is by definition
#define UINT_MIN 0

int main(){
    printf("UINT_MIN: %u\n", UINT_MIN); 
    printf("UINT_MAX: %u\n", UINT_MAX);
    printf("LONG_MAX: %ld\n", LONG_MAX);
    printf("LONG_MIN: %ld\n", LONG_MIN);

    if(LONG_MIN <= UINT_MIN && LONG_MAX >= UINT_MAX){
        printf("`long` can represent all values of `unsigned int`\n");
    }
    return 0;
}
