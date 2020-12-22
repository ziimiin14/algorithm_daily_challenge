#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s_dict = {}
    
    for x in s:
        if x not in s_dict:
            s_dict[x] = 1
        else:
            s_dict[x] += 1
            

    count_dict = {}
    for x,y in s_dict.items():
        if y not in count_dict:
            count_dict[y] = 1
        else:
            count_dict[y] += 1
            
    if len(count_dict) == 1:
        return 'YES'
 
    for j,k in count_dict.items():
        if j == 1 and k == 1:
            count_dict[j] -= 1
            break
        if k == 1 and j != 1:
            if j-1 in count_dict:
                count_dict[j-1] += 1
                count_dict[j] -= 1
                break
         
    count = 0
    
    for i in count_dict.values():
        if i > 0:
            count +=1
            
    if count == 1:
        return 'YES'
    
    else:
        return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

