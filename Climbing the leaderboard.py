import math
import os
import random
import re
import sys



def climbingLeaderboard(ranked, player):
    
    ranked = sorted(list(set(ranked)),reverse=True)
    player.sort(reverse = True)
    result = []
    j = 0
    l = len(ranked)
    
    for i in range(len(player)):
        while j < l and player[i] < ranked[j]:
            j+=1
        result.append(j+1)
        
    return result[::-1]
            
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

