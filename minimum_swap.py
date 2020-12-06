#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0 
    n = len(arr)
    m = 0 
    middle = n//2
    check = True
    

        
    while(check):
        if m < n:
            if arr[m] != m+1:
                arr[arr[m]-1],arr[m] = arr[m], arr[arr[m]-1]
                swap += 1
            
            else:
                m+=1
        else:
            check = False

    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
