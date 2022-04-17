def Fibonacci_Number(n):

    F1 = 0
    F2 = 1
    

    if n==0:
        return 0

    elif n<0:
        print("Enter only positive integer!")
        return ""
    
    else:
        for i in range (1, n):
            F = F1+F2
            F1 = F2
            F2 = F
        return F2
    


n = int(input("Enter the position:\n"))
print(f"The fibonacci number at position {n} is:")
print(Fibonacci_Number(n))
