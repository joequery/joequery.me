#include <stdio.h>
#include <limits.h>
int main(){
    unsigned long ul = (unsigned long) -1L;
    printf("%lu\n", ul);

    // Compare
    printf("%lu\n", ULONG_MAX);
    return 0;
}
