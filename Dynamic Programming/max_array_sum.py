#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_sums = [0]*len(arr)
    max_sums[len(arr)-1] = max(arr[-1], 0)
    max_sums[len(arr)-2] = max(arr[len(arr)-2], arr[len(arr)-1], 0)
    max_sums[len(arr)-3] = max(arr[len(arr)-3]+arr[len(arr)-1], arr[len(arr)-3], arr[len(arr)-2], arr[len(arr)-1], 0)
    for i in range(len(arr)-4,-1,-1):
        max_sums[i] = max(arr[i]+max_sums[i+2], max_sums[i+2], arr[i+1]+max_sums[i+3], max_sums[i+3])
    return max_sums[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
