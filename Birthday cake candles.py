

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    count = 0
    max1 = candles[0]
    for number in candles:
        if number>max1:
            max1 = number
            count = 1
        elif number==max1:
            count+=1 #increase count by 1

    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

