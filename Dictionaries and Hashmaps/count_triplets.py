#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    triplets = {}
    for i in range(len(arr)):
        if (arr[i]%(r*r)==0 and arr[i]//(r*r) in triplets):
            triplets[arr[i]//(r*r)][2] += triplets[arr[i]//(r*r)][1]
        if (arr[i]%r==0 and arr[i]//r in triplets):
            triplets[arr[i]//r][1] += triplets[arr[i]//r][0]
        if (arr[i] in triplets):
            triplets[arr[i]][0]+=1
        else:
            triplets[arr[i]]=[1,0,0]
    num_triplets = 0
    for num in triplets:
        num_triplets += triplets[num][2]
    return num_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()