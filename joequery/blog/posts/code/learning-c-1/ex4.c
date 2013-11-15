#include <stdio.h>
#define MYNAME "Joseph"
#define YOURNAME "Dork"
int main(){
    printf("Hello YOURNAME, My name is MYNAME\n");
    printf("Hello %s, My name is %s\n", YOURNAME, MYNAME);
    return 0;
}
