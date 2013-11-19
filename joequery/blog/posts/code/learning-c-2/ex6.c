#include <stdio.h>
#include <math.h>
int main(){
    // You need a grade average of 70 after rounding to graduate
    int graduation_threshold = 70;
    float your_grade = 69.9999;
    float your_grade_rounded = round(your_grade);
    printf("Your rounded grade as a double: %.2f\n", your_grade_rounded);

    int your_grade_as_int = your_grade;
    int your_grade_as_int_rounded = round(your_grade_as_int);

    if(your_grade_as_int_rounded >= graduation_threshold){
        printf("You graduated. Congrats!\n");
    }
    else{
        printf("You failed! Oh no!\n");
    }
    printf("Your final grade: %d\n", your_grade_as_int_rounded);

    return 0;
}
