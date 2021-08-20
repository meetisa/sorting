import sys
import os
import random as rn
import time
from utils.formatting.textcolors import *

'''This algorithm is a shaker sort program, with a textual-graphical
rapresentation of sorting the array.
The array that will be sorted is a vector<int> of variable length,
made of random numbers of the range 0-100.
If you are searching for an explanation of bubble sort check
the README.md in this folder.

The script accepts some arguments in the terminal:
-first argument should be the length of the array. Default is 20.
-second argument should be <graphic=true> or <graphic=false>
(without brackets) deciding if showing the graphic rapresentation,
otherwise it will print only the sorted array and time of execution.
Default is true.
-third argument should be wrote only if second argument is true.
<clear> or <no-clear> (without brackets), denoting the formatting
of the graphical rapresentation. If <clear> then the screen will
be cleared after every swapped couple. Default is <clear>.
'''

class Main:
    def __init__(self, length, graphics, clear):
        self.graphics, self.clear = graphics, clear
        
        self.start_time = time.time()

        # Creating two equal array:
        # One for the real alg,
        # One for the graphical rapresentaion
        arr1 = [rn.randint(1, 100) for _ in range(length)]
        arr2 = arr1.copy()

        # Auto-starting the program in the costructor
        self.execution(arr1, arr2)

    def execution(self, arr1, arr2):
        self.bubble(arr1)
        if self.graphics:
            self.graphical_bubble(arr2)
        print(*arr1)

    def bubble(self, arr: list):
        # Initialized needed vars
        swapped = True

        # Main while loop
        while swapped:
            swapped = False
            # Left-to-right for loop
            for i in range(len(arr)-1):
                # Main if statement
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            # Right-to-left for loop
            for i in range(len(arr)-2, -1, -1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True

        # Calculating time of execution
        self.execution_time = (time.time() - self.start_time)

    def graphical_bubble(self, arr: list):
        arr = ColoredArray(arr, 'white', 'black')

        # Initializing needed vars
        iterations = n_swapped = 0
        swapped = True

        # Main loop
        while swapped:
            iterations += 1
            swapped = False
            
            # Left-to-right for loop
            for i in range(len(arr.array)-1):
                
                # Main if statement
                if int(arr.array[i].text) > int(arr.array[i+1].text):

                    # Coloring elements to be swapped -> swapping elements
                    arr.coloring_indexes([i, i+1], 'black', 'red')
                    arr.array[i], arr.array[i+1] = arr.array[i+1], arr.array[i]
                    
                    # Graphical commands
                    arr.print_elements()
                    time.sleep(.5)
                    if self.clear:
                        os.system('clear')
                    
                    # Updating vars
                    n_swapped += 1
                    swapped = True

                # Reset all elements' style
                arr.coloring_indexes(range(len(arr.array)), 'white', 'black')

            if not swapped:
                break

            iterations += 1
            swapped = False

            # Right-to-left for loop
            for i in range(len(arr.array)-2, -1, -1):
                
                # Main if statement
                if int(arr.array[i].text) > int(arr.array[i+1].text):

                    # Coloring elements to be swapped -> swapping elements
                    arr.coloring_indexes([i, i+1], 'black', 'red')
                    arr.array[i], arr.array[i+1] = arr.array[i+1], arr.array[i]
                    
                    # Graphical commands
                    arr.print_elements()
                    time.sleep(.5)
                    if self.clear:
                        os.system('clear')
                    
                    # Updating vars
                    n_swapped += 1
                    swapped = True

                # Reset all elements' style
                arr.coloring_indexes(range(len(arr.array)), 'white', 'black')
                

        # Printing all elements, the final array should be sorted
        arr.print_elements()

        # Printing all the specifications
        print(f'Total iterations:{iterations}')
        print(f'Total number of swapped elements:{n_swapped}')


if __name__ == '__main__':
    argv = sys.argv[1:]
    
    if len(argv) >= 1:
        length = int(argv[0])
        if len(argv) >= 2:
            graphics = True if argv[1] == 'graphic=true' else False
            if len(argv) == 3:
                clear = True if argv[2] == 'clear' else False
            else:
                clear = True
        else:
            graphics = True
            clear = True
    else:
        length = 20
        graphics = True
        clear = True
        
    execution_time = Main(length, graphics, clear).execution_time
    print("--- %.5f seconds ---" % execution_time)
