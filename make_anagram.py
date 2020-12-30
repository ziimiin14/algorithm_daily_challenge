#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    g = {}
    h = {}

    for x in s1:
        if x not in g:
            g[x] = 1
        else:
            g[x] += 1
    
    for y in s2:
        if y not in h:
            h[y] = 1
        else:
            h[y] += 1
    count = 0
    for x in g:
        if x not in h:
            count += g[x]
            g[x] = 0
        else:
            if abs(g[x]-h[x]) != 0:
                count += abs(g[x]-h[x])
                if g[x] > h[x]:
                    g[x] -= count
                else:
                    h[x] -= count  
        
    for y in h:
        if y not in g:
            count += h[y]
            h[y] = 0

    return count
            
    
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

