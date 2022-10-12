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
    s = []
    if m == 0:
        s = [convertNumToStr(h), "o' clock"]
    elif m % 15 == 0:
        s.append("half" if m == 30 else "quarter") 
        s.append("to" if m == 45 else "past") 
        s.append(convertNumToStr(h + 1 if m == 45 else h))
    else:
        s.append(convertNumToStr(m if m < 30 else 60 - m))
        s.append("minute" if m == 1 or m == 59 else "minutes")
        s.append("past" if m < 30 else "to")
        s.append(convertNumToStr(h if m < 30 else h + 1))
        
    return " ".join(s)

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
