list1 = [23, 43, 2, 65, 45]
n=len(list1)

for i in range (n):
    min_index = i
    for j in range (i+1, n):
        if list1[min_index] > list1[j]:
            min_index = j

    temp = list1[i]
    list1[i] = list1[min_index
    list1[min_index] = temp
    print(list1)

print("Sorted: ", list1)
