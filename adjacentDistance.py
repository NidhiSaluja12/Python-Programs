def adjacentDistance(n, arr):
    distance = 0
    for i in range(n-1):
        difference = abs(arr[i+1] - arr[i])
        distance += difference
    return distance

n = int(input("Enter number of elements of the list:\n"))
arr = list(map(int, input().split()))
result = adjacentDistance(n, arr)
print(result)
