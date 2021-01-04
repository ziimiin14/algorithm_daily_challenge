#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    m = []
    if k == 1:
        return 1
    if k == 0:
        return 0
    for x in s:
        m.append(x%k)
    temp = [0]*k
    
    for x in m:
        temp[x] += 1
    
    for i in range(1,len(temp)):
        if temp[i] >0:
            if temp[k-i]>0:
                if temp[i]> temp[k-i]:
                    temp[k-i] = 0
                else:
                    temp[i] = 0
    if temp[0] >1 :
        temp[0] = 1
    count = sum(temp)
    if k%2 == 0:
        count +=1
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

