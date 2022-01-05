import math
import os
import random
import re
import sys


def cutTheSticks(arr):
    result = []
    
    while len(arr)>=1:
        result.append(len(arr))
        min1 = min(arr)
        arr = [i-min1 for i in arr if i!=min1]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

