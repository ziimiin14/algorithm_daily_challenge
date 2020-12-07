#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    curr = 0
    c = sorted(c)
    print(c)
    for i in range(len(c)-1):
        temp = c[i]
        temp1 = c[i+1]
        temp2 = abs(temp1-temp)//2

        if temp2> curr:
            curr = temp2
        
    if c[-1] < n-1:
        temp3 = n-1-c[-1]
        if temp3 > curr:
            curr = temp3
    
    if c[0] > 0:
        temp4 = c[0]-0
        if temp4 > curr:
            curr = temp4
    
    return curr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
