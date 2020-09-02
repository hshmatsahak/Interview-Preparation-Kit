#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    min_candies = 1
    i = 0
    while i+1 < len(arr):
        min_candies-=1
        upcount = 1
        downcount = 1
        while i+1<len(arr) and arr[i]==arr[i+1]:
            min_candies +=1
            i+=1
        while i+1<len(arr) and arr[i]<arr[i+1]:
            upcount+=1
            i+=1
        while i+1<len(arr) and arr[i]>arr[i+1]:
            downcount+=1
            i+=1
        if (upcount>=downcount):
            downcount-=1
        else:
            upcount-=1
        print(upcount)
        print(downcount)
        min_candies+=(downcount*(downcount+1)+upcount*(upcount+1))//2
        print(min_candies)
        #i+=1
    return min_candies

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()