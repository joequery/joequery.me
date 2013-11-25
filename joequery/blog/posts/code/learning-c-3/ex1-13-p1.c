#include <stdio.h>
void make_histogram(int arr[], size_t n);

int main(){
    int word_lengths[] = {0, 3, 6, 5};
    make_histogram(word_lengths, 4);
    return 0;
}

// 3 <= n <= 9
void make_histogram(int arr[], size_t n){
    int i, maxval;

    // 0 length words don't mean anything, skipping over them.
    maxval = arr[1];
    for(i=2; i<n; i++)
        if(arr[i] > maxval)
            maxval = arr[i];

    while(maxval > 0){
        for(i=1; i<n; i++){
            if(arr[i] >= maxval)
                putchar('|');
            else
                putchar(' ');
        }
        putchar('\n');
        maxval--;
    }

    // Print footer
    for(i=1; i<n; i++){
        putchar('0'+i);
    }
    putchar('\n');

}
