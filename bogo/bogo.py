import sys
import os
import random as rn
import time
from utils.formatting.textcolors import *

'''This algorithm is a bogo sort program, with a textual/video
graphical rapresentation of sorting the array.
Warning: this sorting algorithm is not stable, it may take forever to
sort the array.
The array that will be sorted is a vector<int> of variable length,
made of random numbers of the range 0-100. Default length is 20.
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
        print(*arr1)

        # Auto-starting the program in the costructor
        self.execution(arr1, arr2)

    def execution(self, arr1, arr2):
        self.bogo(arr1)
        if self.graphics:
            self.graphical_bogo(arr2)
        print(*arr1)

    def bogo(self, arr: list):
        # Initializing needed var
        ordered = False

        # Main while loop
        while not ordered:
            rn.shuffle(arr)
            # Main for loop
            for i in range(len(arr)-1):
                # Main if loop
                if arr[i] > arr[i+1]:
                    ordered = False
                    break
            else:
                ordered = True

        # Calculating time of execution
        self.execution_time = (time.time() - self.start_time)

    def graphical_bogo(self, arr: list):
        arr = ColoredArray(arr, 'white', 'black')

        # Initializing needed vars
        iterations = 0
        ordered = False
        ord_arr = sorted([int(x.text) for x in arr.array])

        # Main loop
        while not ordered:
            iterations += 1
            rn.shuffle(arr.array)

            # Coloring elements to be swapped -> swapping elements
            arr.coloring_indexes(
                [
                    x
                    for x in range(len(arr.array))
                    if int(arr.array[x].text) != ord_arr[x]
                ],
                'black',
                'red'
            )
                    
            # Graphical commands
            arr.print_elements()
            time.sleep(.5)
            if self.clear:
                os.system('clear')
        
            # Main for loop
            for i in range(len(arr.array)-1):
                if int(arr.array[i].text) > int(arr.array[i+1].text):
                    # Updating var
                    ordered = False
                    break
            else:
                ordered = True

            # Reset all elements' style
            arr.coloring_indexes(range(len(arr.array)), 'white', 'black')

        # Printing all the specifications
        print(f'Total iterations:{iterations}')

    def video_graphical_bubble(self):
        pass


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
