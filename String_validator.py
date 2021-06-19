s = input()
a, b, c, d, e = False, False, False, False, False
lst = list(s)
for i in lst:
    if i.isalnum():
        a = True

    if i.isalpha():
        b = True

    if i.isdigit():
        c = True

    if i.islower():
        d = True

    if i.isupper():
        e = True

if __name__ == '__main__':
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

