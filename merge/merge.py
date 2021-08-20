import os
import random as rn
import time
from itertools import groupby
from utils.formatting.textcolors import *


class Main():
    def __init__(self):
        self.start_time = time.time()
        arr1 = [rn.randint(0, 100) for x in range(20)]
        arr2 = arr1.copy()
        self.arrays = []     
        self.execution(arr1, arr2)

    def execution(self, arr1, arr2):
        self.merge(arr1)
        self.execution_time = time.time() - self.start_time
        self.graphical_merge(arr2)
        print(*arr2)
        print(*arr1)

    def merge(self, arr):
        if len(arr) > 1:
            center = len(arr) // 2
            left, right = arr[:center], arr[center:]
            
            self.merge(left)
            self.merge(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def graphical_merge(self, arr):
        pass


if __name__ == '__main__':
    execution_time = Main().execution_time
    print("--- %.6f seconds ---" % execution_time)
