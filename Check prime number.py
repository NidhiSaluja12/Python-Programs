def check_prime_number(n):
    result = 0
    if n > 1:
        for i in range (2, n):
            if n % i == 0:
                result = "NO"
                break

            else:
               result = "YES"
    else:
       result = "NO"
    return result


n = int(input())
res = check_prime_number(n)
print(res)
