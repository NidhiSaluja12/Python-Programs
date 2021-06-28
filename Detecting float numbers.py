T = int(input())
for i in range(T):
    N = input()
    try:
        f = float(N)
        s = int(N.split(".")[1])
        
        print(True)
    except Exception:
        print(False)
        
