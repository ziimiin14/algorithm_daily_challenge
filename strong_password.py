#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    check = [0,0,0,0]
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    for i in range(n):
        if password[i] in numbers:
            check[0] = 1
        if password[i] in lower_case:
            check[1] = 1
        if password[i] in upper_case:
            check[2] = 1
        if password[i] in special_characters:
            check[3] = 1
    total = 0
    for x in check:
        if x == 0:
            total += 1
    if n < 6:
        if total < 6-n:
            total = 6-n
        
    return total
        
    
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

