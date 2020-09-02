#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    minm = float('inf')
    for i in range(len(arr)-1):
        if (abs(sorted_arr[i]-sorted_arr[i+1])<minm):
            minm = abs(sorted_arr[i]-sorted_arr[i+1])
    return minm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
