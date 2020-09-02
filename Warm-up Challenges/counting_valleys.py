#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    enter_valley = False
    status = 0
    num_valleys = 0
    for i in range(n):
        if (s[i] == 'U'):
            status+=1
        else:
            status-=1
        if (enter_valley and status==0):
            num_valleys += 1
            enter_valley = False
        elif (not enter_valley and status == -1):
            enter_valley = True
    return num_valleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
