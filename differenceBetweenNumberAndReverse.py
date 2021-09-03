# Difference between an integer and the reverse of integer. Example : 123 - 321 = -198 ; -123 - (-321) = 198

def difference(n):
    rev = 0

    if n < 0:
        n = n * (-1)

    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n = n // 10

    return rev


n = int(input())

if n > 0:
    result = n - difference(n)
elif n < 0:
    result = n + difference(n)

print(result)
