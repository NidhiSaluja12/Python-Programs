# 32 25 26 5 15 Output = 41

def leader(arr):
    sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                leader1 = arr[i]



    return leader1+arr[len(arr)-1]

arr = list(map(int, input().split()))
print(leader(arr))
