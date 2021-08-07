#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    ins_element = arr[n-1]
    i = n-2
    while i >= 0 and ins_element < arr[i]:
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
        
    arr[i+1] = ins_element
    print(*arr)
        
        
    
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

