#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    
    weight = []
    weight.append(ord(s[0])-96)
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        temp = (ord(s[i])-96)*count
        weight.append(temp)
    weight = set(weight)
    for x in queries:
        if x in weight:
            print('Yes')
        else:
            print('No')
        

if __name__ == '__main__':
    
    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    weightedUniformStrings(s, queries)


