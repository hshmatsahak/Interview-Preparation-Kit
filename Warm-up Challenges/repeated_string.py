#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    pattern_length = len(s)
    last_count = 0
    pattern_count = 0
    last_part = n%pattern_length
    for i in range(last_part):
        if (s[i] == 'a'):
            last_count+=1
            pattern_count+=1
    for i in range(last_part, pattern_length):
        if (s[i] == 'a'):
            pattern_count+=1
    return pattern_count*(n//pattern_length)+last_count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
