def ratCountHouse(rats, unit, array, size):
    
    output = 0
    totalFoodRequired = rats * unit
    foodTillNow = 0
    
    if size == 0:
        return -1

    for i in range(size):
        foodTillNow += array[i]
        output += 1
        if foodTillNow >= totalFoodRequired:
            return output

    if totalFoodRequired > foodTillNow:
        return 0


r = int(input())
unit = int(input())
n = int(input())
arr = list(map(int, input().split()))

result = ratCountHouse(r, unit, arr, n)
print(result)
