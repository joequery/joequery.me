    #include <stdlib.h>
    #include <stdio.h>
    #define BUFSIZE 80

    int main(){
        char path[BUFSIZE];
        char *envvar = "PATH";

        // Make sure envar actually exists
        if(!getenv(envvar)){
            fprintf(stderr, "The environment variable %s was not found.\n", envvar);
            exit(1);
        }

        // Make sure the buffer is large enough to hold the environment variable
        // value. 
        if(snprintf(path, BUFSIZE, "%s", getenv(envvar)) >= BUFSIZE){
            fprintf(stderr, "BUFSIZE of %d was too small. Aborting\n", BUFSIZE);
            exit(1);
        }
        printf("PATH: %s\n", path);
        
        return 0;
    }
