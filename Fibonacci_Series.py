def Fibonacci_Series(n):

    F1 = 0
    F2 = 1
    count = 0

    if n<0:
        print("Enter only positive integers!")
        
    elif n==0:
        print(f"Fibonacci series till {n} position is {F1}")

    else:
        print(f"Fibonacci series till {n} position is\n ")
        while count < n:
            print(F1)
            F = F1+F2
            F1 = F2
            F2 = F
            count += 1

n = int(input("Enter the number of elements:\n"))
Fibonacci_Series(n)
