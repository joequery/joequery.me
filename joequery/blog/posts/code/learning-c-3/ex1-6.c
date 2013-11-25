#include <stdio.h>
int main(){
    int expr_val, c;
    printf("Input a character and press enter: ");
    expr_val = (getchar() != EOF);
    printf("expr_val: %d\n", expr_val);

    return 0;
}
