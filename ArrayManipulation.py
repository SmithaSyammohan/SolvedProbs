#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    ll = []
    for i in range(n+1):
        ll.append(0)
    for row in queries:
        a = row[0]
        b = row[1]
        k = row[2]
        ll[a-1] = ll[a-1] + k 
        ll[b] = ll[b] - k
    max_value = 0  
    running_count = 0  
    for element in ll:
        running_count = running_count + element
        if running_count > max_value:
            max_value = running_count
           

    return max_value        

            



   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
