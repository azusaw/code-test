#!/bin/python3
/* azusaw */

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    l = len(s)
    n = int(math.sqrt(l))
    r = n if n * (n + 1) > l else n + 1
    c = n + 1 if n ** 2 != l else n
    res = ""
    for i in range(0, c):
        for j in range(0, r):
            if (i + j * c) < l:
                res += s[i + j * c]
        res += " "
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
