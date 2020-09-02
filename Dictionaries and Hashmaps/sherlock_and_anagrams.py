#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    sumt = 0
    for i in range(1, len(s)+1):
        words = {}
        for j in range(len(s)+1-i):
            substr = s[j:j+i]
            sorted_substr = "".join(sorted(substr))
            if (sorted_substr in words):
                words[sorted_substr] += 1
            else:
                words[sorted_substr] = 1
        for string in words:
            sumt += (words[string]*(words[string]-1))//2
    return sumt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
