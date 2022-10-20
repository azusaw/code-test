#!/bin/python3
# azusaw

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    lw = list(w)
    lw.sort(reverse=True)
    
    # no change
    if lw == list(w):
        return "no answer"
    
    # two letters word
    if len(lw) == 2:
        return ''.join(lw)

    # change from tail
    return ''.join(sortletterOrder(w))

def sortletterOrder(w):
    lw = list(w)    
    for i in range(1, len(lw) + 1):
        for j in range(1, i):
            if (lw[-j] > lw[-i]):
                tmp = lw[-j]
                lw[-j] = lw[-i]
                lw[-i] = tmp
                if (i == 1):
                    return lw
                l = lw[len(lw) - i + 1:]
                l.sort()
                return lw[:len(lw) - i + 1] + l
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
