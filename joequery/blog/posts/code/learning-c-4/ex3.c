#include <stdio.h>
int main(){
    unsigned char c = 57;
    unsigned int i;
    printf("c: %u\n", c);
    printf("~c: %u\n", (unsigned char) ~c);
    printf("~c: %u\n", (unsigned int) ~c);
    return 0;
}
