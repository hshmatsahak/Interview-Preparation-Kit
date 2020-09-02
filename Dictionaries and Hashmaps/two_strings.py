#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_chars = set()
    s2_chars = set()
    for i in range(len(s1)):
        s1_chars.add(s1[i])
    for i in range(len(s2)):
        s2_chars.add(s2[i])
    for i in s1_chars:
        if i in s2_chars:
            return "YES"
            return 
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
