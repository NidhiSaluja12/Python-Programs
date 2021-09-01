def encodeAsNumber(number, data):
    count = 0
    while number > 0:
        digit = number % 10
        if digit == data:
            count += 1
        number = number // 10

    return count


n = int(input("Enter the number:\n"))
d = int(input())
result = encodeAsNumber(n, d)
print(result)
