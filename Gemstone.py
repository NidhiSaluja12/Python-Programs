import math
import os
import random
import re
import sys


def gemstones(arr):
    
    res = set(arr[0])
    
    for i in range(1, len(arr)):
        temp = set(arr[i])
        res = res.intersection(temp)
        
    return len(res)
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
