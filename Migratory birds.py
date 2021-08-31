import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    
    arr.sort()
    max1 = 1
    count = 1
    for i in range(len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            count=1
        if count>max1:
            max1 = count
            ans = arr[i]
    return ans
    
   
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

