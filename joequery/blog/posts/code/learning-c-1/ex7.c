#include <stdio.h>

void copy(char *fromstr, char *tostr);
int main(){
    char buf[10];
    char str[] = "hello";
    copy(str, buf);

    // prints "hello"
    printf("%s\n", buf);
    return 0;
}

void copy(char *fromstr, char *tostr){
    // This works because A) the null char returns 0, which causes the condition
    // to terminate through B) the fact that assignments return the assign
    // value.
    while(*tostr++ = *fromstr++);
}
