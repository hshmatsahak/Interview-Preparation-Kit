#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    sorted_arr=sorted(arr)
    min_unfairness = float('inf')
    for i in range(len(arr)-k+1):
        if (sorted_arr[i+k-1]-sorted_arr[i]<min_unfairness):
            min_unfairness = sorted_arr[i+k-1]-sorted_arr[i]
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
