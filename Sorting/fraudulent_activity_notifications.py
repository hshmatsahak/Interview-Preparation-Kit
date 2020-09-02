#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    count = [0]*201
    for i in range(d):
        count[expenditure[i]:] = [x+1 for x in count[expenditure[i]:]]
    if (d%2==0):
        for i in range(len(expenditure)-d):
            transaction_today = expenditure[i+d]
            min_median = transaction_today/2.0
            if (count[math.floor(min_median)]>d//2):
                notifications+=1
            elif count[math.floor(min_median)]==d//2:
                to_sort = expenditure[i:i+d]
                to_sort.sort()
                if (to_sort[d//2]+to_sort[d//2-1])/2<=min_median:
                    notifications+=1
            count[expenditure[i]:] = [x-1 for x in count[expenditure[i]:]]
            count[expenditure[i+d]:] = [x+1 for x in count[expenditure[i+d]:]]
    else:
        for i in range(len(expenditure)-d):
            transaction_today = expenditure[i+d]
            min_median = transaction_today/2.0
            if (count[math.floor(min_median)]>=(d+1)//2):
                notifications+=1
            count[expenditure[i]:] = [x-1 for x in count[expenditure[i]:]]
            count[expenditure[i+d]:] = [x+1 for x in count[expenditure[i+d]:]]
    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()