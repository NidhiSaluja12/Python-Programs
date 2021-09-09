def differenceOfSum(n, m):
    
    sum1 = 0
    sum2 = 0

    if n > 0 and m > 0:
        
        for i in range(1, m + 1):
            if i % n != 0:
                sum1 += i
            elif i % n == 0:
                sum2 += i
                
    difference = sum1 - sum2

    return difference


n = int(input())
m = int(input())
result = differenceOfSum(n, m)
print(result)
