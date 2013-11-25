#include <stdio.h>
int is_word_separator(char c);
void get_word_lengths(int word_lengths[], size_t n);

int main(){
    int i;
    // Up to length 9. Initialize all to 0.
    int word_lengths[10] = {0};
    get_word_lengths(word_lengths, 10);

    // Print the array elements
    for(i=1; i<10; i++)
        printf("Num words of length %d - %d\n", i, word_lengths[i]);
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

void get_word_lengths(int word_lengths[], size_t n){
    int c, status, length, i;


    printf("Type words! CTRL-D to exit.\n");
    printf("> ");

    status = 0; // 0 => out of word, 1 => inside word
    length = 0; // current word length

    while( (c = getchar()) != EOF ){
        if(status){
            if(is_word_separator(c)){
                status = 0;

                // We are at the end of the word. This is how we keep a tally.
                // Draw it out on a piece of paper if you don't understand :)
                ++word_lengths[length];

                // Reset the word length since we are now finished with the
                // current word.
                length = 0;

                if(c == '\n')
                    printf("> ");
            }
            else{
                length++;
            }
        }
        else{
            if(is_word_separator(c)){
                if(c == '\n')
                    printf("> ");
            }
            else{
                status = 1;

                // We just encountered our first character of the new word
                length = 1;
            }
        }
    }
}
