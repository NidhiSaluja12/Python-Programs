def strongPassword(n, password):
    count = 0
    if any(i.isdigit() for i in password) == False:
        count+=1
        
    if any(i.isupper() for i in password) == False:
        count+=1
    
    if any(i.islower() for i in password) == False:
        count+=1
        
    if any(i in '!@#$%^&*()-+' for i in password) == False:
        count+=1
        
    return max(count, 6-n)

n = int(input())
password = input()
result = strongPassword(n, password)
print(result)

