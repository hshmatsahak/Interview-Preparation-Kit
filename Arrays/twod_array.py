#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxm =  float('-inf')
    for i in range(16):
        row = i // 4
        col = i - 4*row
        row += 1
        col += 1
        curr = arr[row][col]+arr[row-1][col-1]+arr[row-1][col]+arr[row-1][col+1]+arr[row+1][col-1]+arr[row+1][col]+arr[row+1][col+1]
        if (curr>maxm):
            maxm = curr
    return maxm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
