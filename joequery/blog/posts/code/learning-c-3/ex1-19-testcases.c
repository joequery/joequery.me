#include <stdio.h>
#include <assert.h>
#include <string.h>

void test_reverse();
void reverse(char str[], size_t n);
int main(){
    test_reverse();
    printf("reverse() works!\n");
    return 0;
}

/*
 * Reverse a string str with array string length n (don't include null char!)
 * Note: the string passed is altered.
 */
void reverse(char str[], size_t n){
    // To be implemented...
}

/*
 * Set up test cases to help us verify our reverse function works.
 */
void test_reverse(){
    char str[10] = {0}; // Init all elements to \0
    int testnum = 1;

    // Can the function handle odd-length strings?
    strcpy(str, "hello");
    reverse(str, 5);
    assert(strcmp("olleh", str) == 0);
    printf("test %d pass\n", testnum++);

    // Can the function handle even-length strings?
    strcpy(str, "tablet");
    reverse(str, 6);
    assert(strcmp("telbat", str) == 0);
    printf("test %d pass\n", testnum++);

    // What about shorter strings?
    strcpy(str, "hi");
    reverse(str, 2);
    assert(strcmp("ih", str) == 0);
    printf("test %d pass\n", testnum++);

    strcpy(str, "hey");
    reverse(str, 3);
    assert(strcmp("yeh", str) == 0);
    printf("test %d pass\n", testnum++);

    // What about 1-length strings?
    strcpy(str, "i");
    reverse(str, 1);
    assert(strcmp("i", str) == 0);
    printf("test %d pass\n", testnum++);

    // And empty strings?
    strcpy(str, "");
    reverse(str, 0);
    assert(strcmp("", str) == 0);
    printf("test %d pass\n", testnum++);
}
