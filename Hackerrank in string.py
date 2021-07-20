import math
import os
import random
import re
import sys

def hackerrankInString(s):
    hack = 'hackerrank'
    j = 0
    
    for i in s:
        if i == hack[j]:
            j+=1
        if j == len(hack):
            return "YES"
    
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

