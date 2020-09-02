#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    largeRectangle(h, stack)
    return max(stack)

def largeRectangle(h, stack):
    minm = float('inf')
    minidx=-1
    for i in range(len(h)):
        if (h[i]<minm):
            minm=h[i]
            minidx=i
    stack.append(len(h)*minm)
    if (minidx>0):
        largeRectangle(h[:minidx], stack)
    if (minidx<len(h)-1):
        largeRectangle(h[minidx+1:], stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
