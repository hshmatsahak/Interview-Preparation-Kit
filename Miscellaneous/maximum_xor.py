#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    # set depth to 30
    trie = Trie()
    for num in arr:
        trie.insert(num)
    res = []
    for query in queries:
        binary_query = bin(2**32-1-query)[2:]  
        binary_query = '0'*(32-len(binary_query))+binary_query
        curr_node = trie.root
        place_holder = 31
        maxm = 0
        for digit in binary_query:
            if curr_node.children[int(digit)]:
                curr_node = curr_node.children[int(digit)]
                maxm+=2**place_holder
            else:
                curr_node = curr_node.children[1-int(digit)]
            place_holder-=1
        res.append(maxm)
    return res

class TrieNode:
    def __init__(self):
        self.children = [None]*2
        self.isEndNode = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        bin_num = bin(num)[2:]
        bin_num = '0'*(32-len(bin_num))+bin_num
        crawl = self.root
        for level in bin_num:
            if not crawl.children[int(level)]:
                crawl.children[int(level)] = TrieNode()
            crawl = crawl.children[int(level)]
        crawl.isEndNode = True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()