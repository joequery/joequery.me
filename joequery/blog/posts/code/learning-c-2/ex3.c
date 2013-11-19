#include <stdio.h>
int main(){
    int theint = 123;
    printf("%d\n", theint);

    long thelong = 123456789L;
    printf("%ld\n", thelong);

    unsigned theuint = 123U;
    printf("%u\n", theuint);

    unsigned long theulong = 123456789UL;
    printf("%lu\n", theulong);

    double thedouble = 123e-2;
    printf("%f\n", thedouble);

    int thehex = 0xA88BCF;
    printf("%x\n", thehex);

    char thechar = 'A'; // single, not double quotes
    printf("c as char: %c\n", thechar);
    printf("c as int: %d\n", thechar);
    return 0;
}
