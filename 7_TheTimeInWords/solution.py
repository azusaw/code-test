#!/bin/python3
# azusaw

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    if m == 0:
        s = convertNumToStr(h) + " o' clock "
    elif m == 15:
        s = "quarter past " + convertNumToStr(h)
    elif m == 30:
        s = "half past " + convertNumToStr(h)
    elif m == 45:
        s = "quarter to " + convertNumToStr(h + 1)   
    elif m < 30 :
        s = convertNumToStr(m) + " minutes past " + convertNumToStr(h)
    else:
        s = convertNumToStr(60 - m) + " minutes to " + convertNumToStr(h + 1)
    
    if ("one minutes" in s):
        s = s.replace("minutes", "minute")
        
    return s

def convertNumToStr(n):
    numl = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    prefix = ["thir", numl[3], "fif", numl[5], numl[6], "eigh", numl[8]]
    if n < 13:
        return numl[n - 1]
    elif n < 20:
        return prefix[n - 13] + "teen"
    elif n == 20:
        return "twenty"
    return "twenty " + numl[n - 21]
        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
