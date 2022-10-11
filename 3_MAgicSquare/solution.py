#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    res = 100
    ms_list = makeMagicSquare()
    for mc in ms_list:
        t1 = 0
        t2 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                # normal pattern
                t1 += abs(mc[i][j] - s[i][j])
                # reverse pattern
                t2 += abs(mc[i][2-j] - s[i][j])
        res = min(res, t1, t2)
    return res

def makeMagicSquare():
    ms_list=[[[2,9,4],[7,5,3],[6,1,8]]]
    # make rotate pattern
    for i in range(0, 3):
        r = []
        for j in range (0, 3):
            c = []
            for k in range(0, 3):
                c.append(ms_list[i][2-k][j])
            r.append(c)
        ms_list.append(r)
    return ms_list
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
