def CheckPassword(str, n):
    
    output = 0
    num = 0
    cap = 0
    
    if n < 4:
        output = 0
        
    if str[0].isdigit():
        output = 0

    for i in str:
        if i == '/':
            output = 0
        if i.isdigit():
            num += 1
        if i.isupper():
            cap += 1
    
    if cap >= 1 and num >= 1:
        output = 1

    return output

str = input()
n = len(str)
result = CheckPassword(str, n)
print(result)
