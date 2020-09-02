#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    size = {}
    res = []
    parents = {}
    curr_max = 1
    for i in range(len(queries)):
        parent1 = queries[i][0]
        while parent1 in parents:
            parent1 = parents[parent1]
        parent2 = queries[i][1]
        while parent2 in parents:
            parent2 = parents[parent2]
        if parent1==parent2:
            res.append(curr_max)
            continue
        if (parent1 < parent2):
            parent1, parent2 = parent2, parent1
        parents[parent2] = parent1
        if parent1 not in size:
            size[parent1] = 1
        if parent2 not in size:
            size[parent2] = 1
        size[parent1] += size[parent2]
        if (size[parent1]>curr_max):
            curr_max = size[parent1]        
        res.append(curr_max)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()