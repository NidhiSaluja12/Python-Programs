def staircase(n):
    for i in range(1,n+1):
        res=' '*(n-i)+ '#'*i
        print(res)
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

