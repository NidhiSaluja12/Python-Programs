def moveHyphens(str):
    count = 0
    final = ""
    for i in str:
        if i == '-':
            count+=1
        else:
            final+=i
    return print("-"*count,final)


str = input()
result = moveHyphens(str)
print(result)
