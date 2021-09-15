def lengthOfString(str):
    count = 0
    
    for i in str:
        count += 1
        
    return count 

str = input()
print(lengthOfString(str))
