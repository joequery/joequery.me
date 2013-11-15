#include <stdio.h>
int main(){
    // This will cause a compiler error
    extern int somevalue = 10;
    return 0;
}
