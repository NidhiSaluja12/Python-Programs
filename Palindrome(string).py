string = input()
st_len = len(string)
temp = False
for i in range(int(st_len/2)):
    if string[i] == string[st_len - i - 1]:
        temp = True

if temp == True:
    print("Palindrome")
else:
    print("Not palindrome")
