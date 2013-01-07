#include<stdio.h>
#define BUFSIZE 10

int main(){
    char buf[BUFSIZE];
    if(snprintf(buf, BUFSIZE, "hello") >= BUFSIZE){
        printf("%s\n", buf);
    }

    if(snprintf(buf, BUFSIZE, "An extremely long string") >= BUFSIZE){
        printf("buf: %s\n", buf);
    }

    if(snprintf(buf, BUFSIZE, "0%d", 123456789) >= BUFSIZE){
        printf("buf: %s\n", buf);
    }

    return 0;
}
