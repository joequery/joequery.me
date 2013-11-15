#include <stdio.h>
int main(){
    int c;
    printf("Type something! Press enter to echo, CTRL-D to exit\n");
    while ((c = getchar()) != EOF){
        putchar(c);
    }
    return 0;
}
