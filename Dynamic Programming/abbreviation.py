#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    cash = []
    for i in range(len(b)+1):
        temp = []
        for j in range(len(a)+1):
            temp.append(0)
        cash.append(temp)
    cash[len(b)][len(a)] = 1
    for i in range(len(b)):
        cash[i][len(a)] = -1
    for i in range(len(a)):
        if a[i:].lower()==a[i:]:
            cash[len(b)][i]=1
        else:
            cash[len(b)][i]=-1
    for i in range(len(a)-1,-1,-1):
        for j in range(len(b)-1,-1,-1):
            if a[i].islower() and a[i].upper()==b[j]:
                if cash[j][i+1]==1 or cash[j+1][i+1]==1:
                    cash[j][i] = 1
                else:
                    cash[j][i]=-1
            elif a[i]==b[j]:
                cash[j][i] = cash[j+1][i+1]
            elif a[i].isupper() and a[i]!=b[j]:
                cash[j][i] = -1
            else:
                cash[j][i] = cash[j][i+1]
    if (cash[0][0]==1):
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
