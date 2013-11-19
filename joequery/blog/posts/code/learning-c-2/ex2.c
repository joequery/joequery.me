#include <stdio.h>
int main(){
    // --------------------------------------------------
    // Messing with size qualifiers
    // --------------------------------------------------
    short sx = 10;
    int ix = 10;
    long lx = 10;

    char *fmt1 = "short: %zu, int: %zu, long: %zu\n";
    printf(fmt1, sizeof sx, sizeof ix, sizeof lx);

    float fy = 10.0;
    double dy = 10.0;
    long double ldy = 10.0;

    char *fmt2 = "float: %zu, double: %zu, long double: %zu\n";
    printf(fmt2, sizeof fy, sizeof dy, sizeof ldy);

    // --------------------------------------------------
    // Messing with signed/unsigned qualifiers
    // --------------------------------------------------
    unsigned char c = -1;
    unsigned long lc = -1;
    printf("c: %u, lc: %lu\n", c, lc);

    return 0;
}
