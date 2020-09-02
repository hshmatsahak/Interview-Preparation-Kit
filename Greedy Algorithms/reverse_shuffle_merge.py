#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    res = ''
    s = s[::-1]
    bank = {}
    need = {}
    have = [0]*26
    for i in range(len(s)):
        if (s[i] in bank):
            bank[s[i]]+=1
        else:
            bank[s[i]]=1
    for key in bank:
        need[key] = bank[key]//2
    for i in range(len(s)):
        if (need[s[i]]>0):
            bank[s[i]]-=1
            have[ord(s[i])-ord('a')]+=1
            if not s[i] == 'z' and have[ord(s[i])-ord('a')]<=need[s[i]]:
                have[ord(s[i])-ord('a')+1:]=[0]*(25-(ord(s[i])-ord('a')))
            if(bank[s[i]] < need[s[i]]):
                temp=''
                need[s[i]]-=1
                for j in range(ord(s[i])-ord('a')):
                    if chr(97+j) in need:
                        how_many = min(need[chr(ord('a')+j)], have[j])
                        temp = temp+chr(ord('a')+j)*how_many
                        need[chr(97+j)]-=how_many
                res+=temp+s[i]
                have[ord(s[i])-ord('a')]-=1
                if not s[i]=='a':
                    have[:ord(s[i])-ord('a')]=[0]*(ord(s[i])-ord('a'))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()