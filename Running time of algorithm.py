import math
import os
import random
import re
import sys

def runningTime(arr):
    
    count = 0
    for i in range(len(arr)):
        j = i-1
        key = arr[i]
        
        while j >= 0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
            count+=1
        arr[j+1] = key
        
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

