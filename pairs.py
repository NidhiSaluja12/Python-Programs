import math
import os
import random
import re
import sys

def pairs(k, arr):
    
    arr = set(arr)
    pairs = 0
    
    for i in arr:
        if i+k in arr:
            pairs += 1
                
    return pairs
 e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = map(int, raw_input().rstrip().split())

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

