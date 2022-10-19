#!/bin/python3
# azusaw

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    obs_r = list(filter(lambda v: v[0] == r_q, obstacles))
    obs_c = list(filter(lambda v: v[1] == c_q, obstacles))
    obs_d = list(filter(lambda v: v[0] - v[1] == r_q - c_q or v[0] + v[1] == r_q + c_q, obstacles))
    cnt = 0
    
    # row direction
    if len(obs_r) == 0:
        cnt += n - 1
    else:
        for i in range(1, c_q):
            if [r_q, c_q - i] in obs_r:
                break
            cnt += 1
        for i in range(1, n - c_q + 1):
            if [r_q, c_q + i] in obs_r:
                break
            cnt += 1
    # col direction
    if len(obs_c) == 0:
        cnt += n - 1
    else:
        for i in range(1, r_q):
            if [r_q - i, c_q] in obs_c:
                break
            cnt += 1
        for i in range(1, n - r_q + 1):
            if [r_q + i, c_q] in obs_c:
                break
            cnt += 1
    # diagonal direction
    for i in range(1, n - r_q + 1):
        if [r_q + i, c_q - i] in obs_d or r_q + i > n or c_q - i < 1:
            break
        cnt += 1
    for i in range(1, n - r_q + 1):
        if [r_q + i, c_q + i] in obs_d or r_q + i > n or c_q + i > n:
            break
        cnt += 1
    for i in range(1, n - c_q + 1):
        if [r_q - i, c_q + i] in obs_d or r_q - i < 1 or c_q + i > n:
            break
        cnt += 1
    for i in range(1, r_q):
        if [r_q - i, c_q - i] in obs_d or r_q -i < 1 or c_q - i < 1:
            break
        cnt += 1
    return cnt
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
