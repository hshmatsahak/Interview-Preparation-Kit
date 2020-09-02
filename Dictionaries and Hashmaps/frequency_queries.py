#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    results = []
    num_to_freq={}
    freq_to_num={}
    for i in range(len(queries)):
        if (queries[i][0] == 1):
            if (queries[i][1] not in num_to_freq):
                num_to_freq[queries[i][1]]=1
                if (1 not in freq_to_num):
                    freq_to_num[1] = [queries[i][1]]
                else:
                    freq_to_num[1].append(queries[i][1])
            else:
                freq_to_num[num_to_freq[queries[i][1]]].remove(queries[i][1])
                num_to_freq[queries[i][1]]+=1
                if (num_to_freq[queries[i][1]] in freq_to_num):
                    freq_to_num[num_to_freq[queries[i][1]]].append(queries[i][1])
                else:
                     freq_to_num[num_to_freq[queries[i][1]]] = [queries[i][1]]
        elif (queries[i][0]==2 and queries[i][1] in num_to_freq):
            freq_to_num[num_to_freq[queries[i][1]]].remove(queries[i][1])
            num_to_freq[queries[i][1]]-=1
            if (num_to_freq[queries[i][1]] in freq_to_num):
                freq_to_num[num_to_freq[queries[i][1]]].append(queries[i][1])
            else:
                freq_to_num[num_to_freq[queries[i][1]]] = [queries[i][1]]
            if (num_to_freq[queries[i][1]]==0):
                num_to_freq.pop(queries[i][1])
        elif (queries[i][0]==3):
            if (queries[i][1] in freq_to_num and freq_to_num[queries[i][1]]!=[]):
                results.append(1)
            else:
                results.append(0)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
