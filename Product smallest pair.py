def ProductSmallestPair(sum, arr):
    n = len(arr)
    if n < 2:
        return -1

    arr = sorted(arr)
    for i in range(n - 1):
        if arr[i] + arr[i + 1] <= sum:
            product = arr[i] * arr[i + 1]
            break

    if product:
        return product
    else:
        return 0


sum = int(input())
arr = list(map(int, input().split()))
result = ProductSmallestPair(sum, arr)
print(result)
