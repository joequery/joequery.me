#include <stdio.h>
#include <limits.h>
int main(){
    unsigned char c = 0;
    printf("c: %u\n", c);
    printf("~c: %u, UCHAR_MAX: %u\n", (unsigned char) ~c, UCHAR_MAX);
    return 0;
}
