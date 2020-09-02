#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    num = 0
    qlen = len(q)
    for i in range(qlen, 1, -1):
        if (q[-1]!=i):
            if (q[-2] == i): 
                num+=1
                q.pop(-2)
            elif (q[-3] == i): 
                num+=2
                q.pop(-3)
            else: 
                print("Too chaotic")
                return
        else:
            q.pop(-1)
    print(num)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
