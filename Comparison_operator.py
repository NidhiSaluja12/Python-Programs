name = input("Enter your name: ")

if len(name) < 3:
    print('Name must contain atleast 3 characters.')

elif len(name) > 50:
    print('Name must be maximum of 50 character.')
else:
    print('Name looks good!!')
