def swappingTwoNumbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("After swapping:\na:", a,"and b:",b)

a = int(input("a: "))
b = int(input("b: "))
swappingTwoNumbers(a, b)
