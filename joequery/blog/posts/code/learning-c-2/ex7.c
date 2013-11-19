#include <stdio.h>
enum category { DOG, HUMAN, CAT };
struct mammal {
    char *name;
    enum category c;
};

void find_the_mammal(struct mammal *mammals, enum category mammal_type, size_t n);
int main(){
    struct mammal mammals[3];
    mammals[0] = (struct mammal){"Joseph", HUMAN};
    mammals[1] = (struct mammal){"Odin", CAT};
    mammals[2] = (struct mammal){"LUCY", DOG};

    find_the_mammal(mammals, HUMAN, 3);
    find_the_mammal(mammals, CAT, 3);
    find_the_mammal(mammals, DOG, 3);
    return 0;
}

void find_the_mammal(struct mammal *mammals, enum category mammal, size_t n){
    int i;
    for(i=0; i<n; i++){
        if(mammals[i].c == mammal)
            printf("%s\n", mammals[i].name);
    }
}
