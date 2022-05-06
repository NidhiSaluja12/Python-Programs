#!/bin/python3
import math
import os
import random
import re
import sys


def breakingRecords(scores):
    dMost = scores[0]
    dLeast = scores[0]
    most = 0
    least = 0
    for score in scores:
        if dMost < score:
            dMost = score
            most+=1
        elif dLeast > score:
            dLeast = score
            least+=1
    return [most,least]
    
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

