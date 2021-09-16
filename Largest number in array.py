def largestNumber(arr):
    largest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    print("Largest number is:", largest, "at the position",index)


arr = list(map(int, input().split()))
largestNumber(arr)
