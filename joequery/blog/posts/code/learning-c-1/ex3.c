#include <stdio.h>
int main(){
    int x = 10;
    float y = 10.0; // float for decimals
    char *mystr = "Hahah";

    printf("x: %d\n", x);
    printf("y: %f\n", y);
    printf("mystr: %s\n", mystr);

    // padding
    printf("x: %5d\n", x);

    // Limit the number of decimal points
    printf("y: %.2f\n", y);

    // Padding AND limit decimal points
    printf("y: %10.2f\n", y);
    return 0;
}
