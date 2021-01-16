#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    first = set()
    check = False
    for i in range(1,101):
        for x in a:
            if i%x == 0:
                check = True
            else:
                check = False
                break
        if check == True:
            first.add(i)
    
    second = set()
    check1 = False
    for x in first:
        for y in b:
            if y%x== 0:
                check1 = True
            else:
                check1 = False
                break
        if check1 == True:
            second.add(x)
            

    return len(first&second)
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

