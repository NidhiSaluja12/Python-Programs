#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

   
    length_arr = len(arr)
    neg = sum(x<0 for x in arr)/length_arr
    pos = sum(x>0 for x in arr)/length_arr
    zero = sum(x==0 for x in arr)/length_arr
    print('{0:.6f}'.format(pos),'{0:.6f}'.format(neg),'{0:.6f}'.format(zero),sep="\n")

