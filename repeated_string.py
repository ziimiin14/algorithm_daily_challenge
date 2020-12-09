#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    real = int(n//len(s))
    extra = n%len(s)
    count = 0
    count1 = 0
    for x in s:
        if x == 'a':
            count +=1
    
    for y in s[0:extra]:
        if y == 'a':
            count1 += 1

    finalcount = count * real + count1
    return finalcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

