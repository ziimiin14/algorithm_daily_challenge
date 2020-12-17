#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr = set(arr)
    count = 0
    for i in range(len(arr)):
        temp = arr.pop()
        if (temp+k) in arr:
            count += 1
        if (temp-k) in arr:
             count +=1   
             
    return count
            

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
