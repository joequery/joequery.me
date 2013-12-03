#include <stdio.h>
int main(){
    unsigned char c;
    c = 0;
    printf("c: %u\n", c);
    c = 1;
    printf("~c: %u\n", c);
    c = ~0;
    printf("~c: %u\n", c);
    return 0;
}
