#include <stdio.h>
void print_str(char *s);

int main(){
    char *mystr = "Hello";
    print_str(mystr);
    return 0;
}

void print_str(char *s){
    int i=0;
    char c;
    while(c = *s++)
        printf("%c\n", c);

    if(c == '\0')
        // '\0' is not a printable character, so we need to print something
        // ourselves if we want to see it.
        printf("\\0\n");
}
