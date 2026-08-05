//Question to count the alphabets using C and basic file manipulation 

#include<stdio.h>
#include<ctype.h> // for isalpha , toupper 

int main(int argc, char *argv[]){

    //initializing variables
    int letter_count[26] = {0}; //one bucket per letter all inited to 0
    long total_letters = 0; 
    int ch;

    if(argc !=2){
        printf("Using file: %s <filename>\n", argv[0]); //argv 0 is the prog name and argc 1 is the file we pass 
        return 1; //return true
    } 

    FILE *fp = fopen(argv[1], "r"); // r in reading moide
    if(fp == NULL){
        printf("Couldnt' open file %s\n", argv[1]); // as mentioned argv 1 is the file name 
    }

    //checking char and counting
    while(( ch = fgetc(fp)) != EOF){
        //loop till end of file
        if ((isalpha(ch))){
            letter_count[ch - 'A']++; //updating the letter count bucjket
            total_letters++; //updating total count
        }
    }

    fclose(fp);

    //printing data
    printf("Letter  Count   Frequency\n");
    for(int i=0; i<26; i++){
        double freq = (double)letter_count[i] / total_letters * 100.0; //calc using double(floating points)
        //freq = freq*100.0; //dopesnt 
        printf("%c  %d  %.2f\n",'A'+i, letter_count[i],freq);
    }

    return 0;

}