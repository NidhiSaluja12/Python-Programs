str = input("Enter your string:\n")

u = 0
l = 0

for i in str:
    
    if i.islower() == True:
        l+=1
        
    if i.isupper()==True:
        u+=1

print(f"Number of lower case characters are {l}")
print(f"Number of upper case characters are {u}")

