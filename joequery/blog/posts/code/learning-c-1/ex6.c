#include <stdio.h>
#define BUF_SIZE 100

void readline(char buf[], int bufsize);

int main(){
    char str[BUF_SIZE];
    readline(str, BUF_SIZE);
    printf("%s\n", str);
    return 0;
}

void readline(char buf[], int bufsize){
    int i,c;
    for(i=0; i<bufsize-1 && (c = getchar()) != EOF && c != '\n'; i++){
        buf[i] = c;
    }
    if(c == '\n')
        buf[i++] = c;
    buf[i] = '\0';
}
