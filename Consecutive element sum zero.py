def sumZero(array, size):
    count = 0

    for i in range(size):
        if array[i] == 0:
            count += 1
        for j in range(i + 1, size):
            if array[i] + array[j] == 0:
                count += 1

    if count:
        return 1
    else:
        return 0


arr = list(map(int, input().split()))
n = len(arr)
result = sumZero(arr, n)
print(result)
