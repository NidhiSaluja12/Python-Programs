cube = lambda x:x**3 

def fibonacci(n):
    L1 = []
    if n==0:
        return L1
    elif n==1:
        L1.append(0)
        return L1
    else:   
        L = [0,1]
        count = 0
        F1 = 0
        F2 = 1
        while count<n-2:
            F = F1+F2
            L.append(F)
            F1 = F2
            F2 = F
            count+=1
        return L
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
