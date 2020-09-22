#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    temp = 0
    d = dict()
    co = 0
    sorted_list = sorted(q)
    while q != sorted_list:
        for x in range(len(q)-1):
            if q[x] > q[x+1]: 
                temp = q[x]
                if q[x] in d:
                    d[q[x]] = d[q[x]] + 1
                else:
                    d[q[x]] = 1 
                co = co + 1        
                q[x] = q[x+1]
                q[x+1] = temp

    for x in d:
        if d[x]>2:
            print("Too chaotic") 
            return
          
    print(co)        
   

 

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)