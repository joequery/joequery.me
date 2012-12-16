    #include<stdio.h>
    #include<stdlib.h>

    int main(){
        int bufSize = 10;
        char *mystr = "This is my string!";
        char *buf = malloc(bufSize);

        if(snprintf(buf, bufSize, "%s", mystr) >= bufSize){
            bufSize *= 2;
            printf("Not enough space. Trying %d bytes\n", bufSize);
            free(buf);
            buf = malloc(bufSize);

            if(snprintf(buf, bufSize, "%s", mystr) >= bufSize){
                printf("Still not enough space. Aborting\n");
                exit(1);
            }
        }

        printf("There was enough space!\n");
        printf("buf: %s\n", buf);
        return 0;
    }
