def find_missing_number_from_array(array, size):
    total = (size + 1) * (size + 2) / 2
    sum1 = sum(array)

    if total != sum1:
        return int(total - sum1)
    else:
        return "No missing number!"


arr = list(map(int, input().split()))
n = len(arr)
res = find_missing_number_from_array(arr, n)
print(res)
