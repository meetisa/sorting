#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

void algorithm(void);

int main(int argv, char argc[])
{
    clock_t begin = clock();
    algorithm();
    clock_t end = clock();
    printf("\n--- %.3f seconds ---", (double)(end - begin) / CLOCKS_PER_SEC);
    return 0;
}

void algorithm(void)
{
    int array[] = {2, 3, 4, 5, 8, 7, 6, 1, 10, 9}, t;
    bool swapped;
    
    do {
       swapped = false;
       for(int i=0; i<9; i++) {
            if(array[i] > array[i+1]) {
                t = array[i];
                array[i] = array[i+1];
                array[i+1] = t;
                printf("%d %d\n", array[i], array[i+1]);
                swapped = true;
            }
       }
    } while(swapped);
    
    for(int i=0; i<10; i++)
        printf("%d ", array[i]);
}
