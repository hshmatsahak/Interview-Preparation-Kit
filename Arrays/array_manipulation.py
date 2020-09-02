#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    sums = []
    for i in range(n):
        sums.append(0)
    for i in range(len(queries)):
        sums[queries[i][0]-1] += queries[i][2]
        if queries[i][1] < n:
            sums[queries[i][1]] -= queries[i][2]
    maxm=float('-inf')
    curr = 0
    for i in range(n):
        curr+=sums[i]
        if (curr>maxm): 
            maxm = curr
    return maxm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
