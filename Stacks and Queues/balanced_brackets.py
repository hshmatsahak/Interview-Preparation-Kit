#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    pairmatch = {'{':'}', '[':']', '(':')'}
    stack = []
    stack.append(s[0])
    for bracket in s[1:]:
        if (bracket in pairmatch):
            stack.append(bracket)
        elif len(stack)==0:
            return "NO"
        elif stack[-1] in pairmatch and pairmatch[stack[-1]]==bracket:
            stack.pop()
        else:
            print("NO")
            return "NO"
    if (stack==[]):
        print("YES")
        return "YES"
    print("NO")
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
