#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    s = 0
    k = 0
    t = 0
    f = 1
    sum_list = []
    count = 0
    while k < 4 and t < 4:
        for i in range(0+t, 3+t):       
            for j in range(0+k, 3+k):
                if count!= 3 and count!= 5:
                    s = s + arr[i][j]   
                count = count + 1                      
        sum_list.append(s) 
        k = k + 1  
        s = 0
        count = 0
        if k == 4:         
            t = t + 1
            k = 0

    return max(sum_list)        
 

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
