def nOddNumbers(n):
    arr = []
    for i in range (n):
        if i % 2 != 0:
            arr.append(i)
    return arr

n = int(input())
result = nOddNumbers(n)
print(result)
