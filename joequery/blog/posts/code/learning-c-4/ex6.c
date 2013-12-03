#include <stdio.h>
#define BITMASK ~0x7
int main(){
    unsigned char c = 31;
    printf("c: %u\n", c);
    c = c & BITMASK;
    printf("c: %u\n", c);
    return 0;
}
