#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = len(s)
    top = math.ceil(n**0.5)
    btm = math.floor(n**0.5)
    if top*btm < n:
        btm = top
    a = ''

    for j in range(top):
        for i in range(btm):
            if i*top+j >= n:
                print(a, end = ' ')
                a = ''
                break

            a += s[i*top+j]
            
            if i == btm-1:
                print(a, end = ' ')
                a = ''
            
        
    

if __name__ == '__main__':

    s = input()

    result = encryption(s)


