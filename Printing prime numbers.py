def print_prime_number(s, e):
    prime_numbers = []
    for number in range(s, e+1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                prime_numbers.append(number)
    return prime_numbers


s = int(input())
e = int(input())
res = print_prime_number(s,e)
print(res)
