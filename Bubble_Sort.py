N = int(input("Enter the number number of elements of list:\n"))
print("Enter the elements:\n")
list1 = []
for n in range(0,N):
    elements=int(input())
    list1.append(elements)

print("Unsorted List")
print(list1)


print("Sorting Started....")
for i in range (0,N-1):
    for j in range(0,N-1):
        if list1[j]>list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
    print(list1)




print("Sorted: \n ",list1)

print(list1[-2])





