#!/bin/python3
import statistics
import math
import os
import random
import re
import sys
import statistics
import bisect
def activityNotifications(expenditure, d, n): 
    box = sorted(expenditure[:d]) 
    m = d//2
    def median(arr, d, m):
        if d%2 == 0:
            median = sum(arr[m-1:m+1])/2
        else:
            median = arr[m] 
        return median
    notifs = 0
    for i in range(d, n):
        if expenditure[i] >= 2*median(box,d,m):
            notifs = notifs + 1
        del box[bisect.bisect_left(box,expenditure[i-d])]
        bisect.insort(box, expenditure[i])
    return notifs    

   

  
    


 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d, n)

    fptr.write(str(result) + '\n')

    fptr.close()
