#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
   
    swaps = 0
    sorted_list = sorted(arr)
    while arr != sorted_list:
        for i in range(len(arr)-1):
            if i == (arr[i]-1):
                continue
            swaps = swaps + 1
            new_index = arr[i] - 1
            temp = arr[new_index]
            arr[new_index] = arr[i]
            arr[i] = temp
    return swaps 
 
        
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()