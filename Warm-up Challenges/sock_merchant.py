#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total = 0
    unmatched = {}
    for i in range(n):
        unmatched[ar[i]] = False
    for i in range(n):
        if unmatched[ar[i]]:
            total += 1
            unmatched[ar[i]] = False
        else:
            unmatched[ar[i]] = True
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()