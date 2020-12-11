#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    arr = []
    match_set = {')',']','}'}
    check = True
    #match_dict = {'(':')','[':']','{':'}'}
    
    for x in s:
        if x in match_set:
            if not arr:
                check = False
                break
            if x == ')':
                temp = '('
            if x == ']':
                temp = '['
            if x == '}':
                temp = '{'
                
            temp1 = arr.pop()
            if temp1 != temp:
                check = False
                break
            
        else:
            arr.append(x)
    if len(arr)>0:
        check = False

    if not check:
        return 'NO'
    else:
        return 'YES'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

