#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    num=0
    pos = {}
    for i in range(len(arr)):
        pos[arr[i]] = i
    for i in range(len(arr), 1, -1):
        if (arr[i-1] != i):
            num+=1
            idx = pos[i]
            pos[arr[i-1]] = idx
            pos[i] = i-1
            arr[idx] = arr[i-1]
            arr[i-1] = i
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
