#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    xmax = max(brr)
    xmin = min(brr)
    diff = xmax-xmin+1
    count1 = [0] * diff
    count2 = [0] * diff
    for num1 in arr:
        count1[num1-xmin] += 1
    for num2 in brr:
        count2[num2-xmin] += 1
    
    final = []
    for i in range(xmin,xmax+1,1):
        if count1[i-xmin] != count2[i-xmin]:
            final.append(i)
    
    
    return final
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

