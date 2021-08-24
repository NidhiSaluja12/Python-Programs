def findCount(array, number, difference):
    output = 0
    for i in range(len(array)):
        if abs(array[i] - number) <= difference:
            output += 1
    if output > 0:
        return output
    else:
        return -1


arr = list(map(int, input().split()))
num = int(input())
diff = int(input())
result = findCount(arr, num, diff)
print(result)
