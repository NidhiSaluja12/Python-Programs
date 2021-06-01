n = int(input("Enter number of elements you are going to enter:\n"))
l = []

for i in range(n):
    element = int(input())
    l.append(element)
print(f"Your list is {l}")

count_even = 0
count_odd = 0
for i in range (len(l)):
    if l[i]%2==0:
        count_even+=1
    else:
        count_odd+=1

print(f"Number of even elements are {count_even}")
print(f"Number of odd elements are {count_odd}")
