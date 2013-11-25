#include <stdio.h>
int main(){
    int c, num_tabs, num_blanks, num_newlines;
    num_tabs = num_blanks = num_newlines = 0;

    printf("Enter text. Press CTRL-D when finished\n> ");
    while( (c = getchar()) != EOF ){
        if(c == '\n')
            printf("> ");

        switch(c){
            case '\t':
                num_tabs++;
                break;
            case ' ':
                num_blanks++;
                break;
            case '\n':
                num_newlines++;
                break;
        }
    }
    printf("EOF sent\n");

    printf("num_tabs: %d\n", num_tabs);
    printf("num_blanks: %d\n", num_blanks);
    printf("num_newlines: %d\n", num_newlines);
    return 0;
}
