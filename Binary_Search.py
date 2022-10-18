# to implement binary search, array should be sorted.
def Binary_search(item, list1):
    
 
   lower_bound = 0
    upper_bound = len(list1) - 1
    middle_index = 0

    while lower_bound <= upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        middle_element = list1[middle_index]

        if item == middle_element:
            return middle_index

        elif item < middle_element:
            upper_bound = middle_index-1

        else:
            lower_bound = middle_index + 1

    return -1


list1 = [1,2,3,4,5,6]
item = 4
res  = Binary_search(item,list1)
if res == -1:
    print("Item not found.")
else:
    print(res+1)



