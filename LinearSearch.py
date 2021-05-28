N = int(input("Enter the number of element:\n"))
print("Enter elements:\n")
arr = []

for j in range(N):
    elem = float(input())
    arr.append(elem)

print(arr)

item = float(input("Enter the element to be checked:\n"))
Status = False
arr_len = len(arr)

for i in range(arr_len):
    if arr[i] == item:
        Status = True

if Status == True:
    print(f"{item} is at {i+1} position.")

else:
    print("Element not found.")


