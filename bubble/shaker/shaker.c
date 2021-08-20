#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

void algorithm(void);

int main(int argv, char *argc[])
{
    clock_t begin = clock();
    algorithm();
    clock_t end = clock();
    printf("\n--- %.6f seconds ---\n", (double)(end - begin) / CLOCKS_PER_SEC);
    return 0;
}


void algorithm(void)
{
    srand(time(0));
    
    int n = 20;
    int array[n];
    
    for(int i=0; i<n; i++) {
        array[i] = 1 + rand() % 100;
        printf("%d ", array[i]);
    }
    
    printf("\n");

    bool swapped;
    
    do {
       swapped = false;
       for(int i=0; i<n-1; i++) {
            if(array[i] > array[i+1]) {
                int t;
                t = array[i];
                array[i] = array[i+1];
                array[i+1] = t;
                swapped = true;
            }
       }
       
       if(!swapped)
           break;
           
       swapped = false;
       for(int i=n-2; i>=0; i--) {
            if(array[i] > array[i+1]) {
                int t;
                t = array[i];
                array[i] = array[i+1];
                array[i+1] = t;
                swapped = true; 
            }
       }
    } while(swapped);
    
    for(int i=0; i<n; i++)
        printf("%d ", array[i]);
}
