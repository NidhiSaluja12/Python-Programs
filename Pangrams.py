import math
import os
import random
import re
import sys

def pangrams(s):
    # s = set(s)
    
    # if len(s) == 27:
    #     return "pangram"
    
    # return "not pangram"

    return 'pangram' if len(set(s.lower()))==27 else 'not pangram'
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

