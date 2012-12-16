#include<stdio.h>
#include<string.h>
#define BUFSIZE 10

void init_to_1(char *buf, size_t size);
void print_buf(char *buf);

int main(){
    char buf[BUFSIZE];
    init_to_1(buf, BUFSIZE);
    print_buf(buf);

    // hello there! => 12 characters, > BUFSIZE
    init_to_1(buf, BUFSIZE);
    snprintf(buf, BUFSIZE, "hello there!");
    print_buf(buf);

    // turtles => 7 charaters, < BUFSIZE
    init_to_1(buf, BUFSIZE);
    snprintf(buf, BUFSIZE, "turtles");
    print_buf(buf);

    // turtles => 7 charaters, > BUFSIZE - 5
    init_to_1(buf, BUFSIZE);
    snprintf(buf, BUFSIZE-5, "turtles");
    print_buf(buf);

    return 0;
}

void init_to_1(char *buf, size_t size){
    int i;
    for(i=0; i<size-1; i++){
        buf[i] = '1';
    }
    buf[size-1] = '\0';
}

void print_buf(char *buf){
    int i;
    char c;
    for(i=0; i<BUFSIZE; i++){
        c = buf[i];
        if(c == '\0'){
            printf("\\0");

        }
        else{
            printf("%c", buf[i]);
        }
    }
    printf("\n");
    printf("strlen of buf: %zd\n\n", strlen(buf));
}
