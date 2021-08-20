import random as rn
import time
from utils.formatting.textcolors import *

class Main:
    def __init__(self):
        self.start_time = time.time()
        arr1 = [rn.randint(0, 100) for x in range(20)]
        arr2 = arr1.copy()
        #print(*arr1)
        self.execution(arr1, arr2)

    def execution(self, arr1, arr2):
        self.counting(arr1)
        self.execution_time = time.time() - self.start_time
        self.graphical_counting(arr2)
        print(*arr1)

    def counting(self, arr):
        min_ = min(arr)
        max_ = max(arr)
        c = [0 for x in range(max_ - min_ + 1)]

        for i in range(len(arr)):
            c[arr[i] - min_] += 1

        k = 0
        for i in range(len(c)):
            while c[i] > 0:
                arr[k] = i + min_
                k += 1
                c[i] -= 1

    def graphical_counting(self, arr):
        min_ = min(arr)
        max_ = max(arr)
        c = [0 for x in range(max_ - min_ + 1)]

        for i in range(len(arr)):
            c[arr[i] - min_] += 1
        
        print(*['Frequence array:', *c])

if __name__ == '__main__':
    execution_time = Main().execution_time
    print("--- %.6f seconds ---" % execution_time)
