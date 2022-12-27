#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    if n % 2 == 0:
        return [''.join(['O' for i in range(0, len(grid[0]))]) for i in range (0, len(grid))]
    elif n == 1:
        return grid
    else:
        exp_grid = explosion(grid)
        if n % 4 == 3:
            return exp_grid
        else:
            return explosion(exp_grid)

def explosion(grid):
    exp_grid = [['O' for i in range(0, len(grid[0]))] for i in range (0, len(grid))]
    for x, line in enumerate(grid):
        for y, cell in enumerate(line):
            if cell == 'O':
                exp_grid[x][y] = "."
                if x - 1 >= 0:
                    exp_grid[x - 1][y] = '.'
                if x + 1 < len(grid):
                    exp_grid[x + 1][y] = '.'
                if y - 1 >= 0:
                    exp_grid[x][y - 1] = '.'
                if y + 1 < len(grid[0]):
                    exp_grid[x][y + 1] = '.'
    return [''.join(exp_grid[i]) for i in range(0, len(grid))]
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
