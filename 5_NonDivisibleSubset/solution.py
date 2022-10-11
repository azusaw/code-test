#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    s = [n % k for n in s]
    l = []
    for i in range(0, len(s)):
        cnt = 0
        for j in range(0, len(s)):
            if i != j and (s[i] + s[j]) % k == 0:
                cnt += 1
        l.append(cnt)  
    ss = insertSort([n for n in s], l)
    sf = []
    for n1 in ss:
        f = 0
        for n2 in sf:
            if (n1 + n2) % k == 0:
                f = 1
                break
        if f == 0:
            sf.append(n1)
    return len(sf)
        

def bubbleSort(s, l):
    change = 1
    while change:
        change = 0
        for i in range(len(s) - 1):
            if l[i] > l[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                l[i], l[i + 1] = l[i + 1], l[i]
                change = 1
    return s

# osoi
def insertSort(s, l):
    for i in range(1, len(s)):
        tmp1 = s[i]
        tmp2 = l[i]
        j = i - 1
        while l[j] > tmp2 and j >= 0:
            s[j + 1] = s[j]
            l[j + 1] = l[j]
            j -= 1
        s[j + 1] = tmp1
        l[j + 1] = tmp2
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
