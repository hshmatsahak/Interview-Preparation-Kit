#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    index = 0
    num_steps = 0
    while(index < len(c)-1):
        if ((index+2<len(c)) and c[index+2] == 0):
            index+=2
        else:
            index+=1
        num_steps+=1
    return num_steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
