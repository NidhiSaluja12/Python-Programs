# Input: comedycomic => Output: 4

def countUniqueElements(str):
    count = 0

    for i in str:
        if str.count(i) < 2:
            count += 1
    return count


str = input()
result = countUniqueElements(str)
print(result)
