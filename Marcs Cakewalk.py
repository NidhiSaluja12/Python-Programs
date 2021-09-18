import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    
    calorie.sort()
    calorie.reverse()
    result = 0
    
    for i in range (len(calorie)):
        res = calorie[i] * (2**i)
        result += res
        
    return result
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

