T = int(input())
for i in range(T):
   
    n = int(input())
    cubes = list(map(int, input().split()))
    length = len(cubes)
    
    if cubes[0]==max(cubes) or cubes[length-1]==max(cubes):
           
        print("Yes")
    else:
          
        print("No")
   
