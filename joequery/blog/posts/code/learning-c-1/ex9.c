#include <stdio.h>
void alter_somevalue();
void alter_somevalue2();
int somevalue = 10;
int main(){
    printf("%d\n", somevalue);
    alter_somevalue();
    printf("%d\n", somevalue);
    alter_somevalue2();
    printf("%d\n", somevalue);
    return 0;
}

void alter_somevalue(){
    extern int somevalue;
    somevalue = 15;
}
void alter_somevalue2(){
    // extern is actually redundant in this case!
    somevalue = 25;
}
