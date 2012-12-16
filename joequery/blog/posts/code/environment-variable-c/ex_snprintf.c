#include <stdio.h>
#define BUF_SIZE 5

int main(){
    char buf[BUF_SIZE];
    //snprintf(buf, BUF_SIZE, "hello");

    for(int i=0; i<BUF_SIZE; i++){
        buf[i] = 'c';
    }

    printf("buf: %s\n", buf);
    return 0;
}
