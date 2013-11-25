#include <stdio.h>
#include <assert.h>
int is_word_separator(char c);
void test_word_separator();

int main(){
    int c, status;
    // First, we test our is_word_separator function.
    // If program execution makes it past this line, our is_word_separator
    // function is good!
    test_word_separator();

    printf("Type words! CTRL-D to exit.\n");
    printf("> ");

    status = 0; // 0 => out of word, 1 => inside word

    while( (c = getchar()) != EOF ){
        // status can be 0 or 1, c can be word separator or not, so we have
        // 2x2=4 cases total to consider.
        if(status){
            if(is_word_separator(c)){
                status = 0;
                // Just for presentation! :)
                if(c == '\n')
                    printf("\n> ");
                else
                    printf("\n");
            }
            else{
                printf("%c", c);
            }
        }
        else{
            if(is_word_separator(c)){
                // Just for presentation! :)
                if(c == '\n')
                    printf("> ");
            }
            else{
                status = 1;
                printf("%c", c);
            }

        }

    }
    printf("EOF sent.\n");
    return 0;
}

int is_word_separator(char c){
    switch(c){
        case '\n':
        case '\t':
        case ' ':
            return 1;
        default:
            return 0;
    }
}

void test_word_separator(){
    assert(is_word_separator('x') == 0);
    assert(is_word_separator(' ') == 1);
    assert(is_word_separator('\n') == 1);
    assert(is_word_separator('\t') == 1);
    assert(is_word_separator('A') == 0);
}
