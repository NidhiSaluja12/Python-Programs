'''Sample Input

STDIN       Function
-----       --------
6 3         n = 6, k = 3
5 1         contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
2 1
1 1
8 1
10 0
5 0

Sample Output
29'''



import math
import os
import random
import re
import sys


def luckBalance(k, contests):
    
    contests.sort(reverse=True)
    luck = 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]

    return luck
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

