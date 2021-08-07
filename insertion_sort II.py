#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        current_index = arr[i]
        pos = i-1
        while pos >= 0 and current_index < arr[pos]:
            arr[pos+1] = arr[pos]
            pos = pos-1
        arr[pos+1] = current_index
        print(*arr)
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

