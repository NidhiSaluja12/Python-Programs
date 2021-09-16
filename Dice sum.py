def diceSum(s):
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i+j == s:
                count += 1
    if count:
        return count
    else:
        return 0

s = int(input())
print(diceSum(s))
