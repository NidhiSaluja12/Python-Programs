import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    
    count =0
    length = len(arr)
    i = 0
    
    while i<length:
        index = arr[i]-1
        if arr[i]!=arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            count+=1
        else:
            i+=1
            
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

