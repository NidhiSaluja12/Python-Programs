def longest_common_substring(str1, str2, n1, n2):

    substring1_list = []
    substring2_list = []
    common_substring = []

    for i in range(n1+1):
        for j in range(i+1, n1+1):
            substring1 = str1[i:j]
            substring1_list.append(substring1)
    print(substring1_list)

    for i in range(n2+1):
        for j in range(i+1, n2+1):
            substring2 = str2[i:j]
            substring2_list.append(substring2)
    print(substring2_list)
    
    if len(substring_list2) < len(substring_list1):
        for i in substring2_list:
            if i in substring1_list:
                common_substring.append(i)
                
     if len(substring_list2) > len(substring_list1):
        for i in substring1_list:
            if i in substring2_list:
                common_substring.append(i)
                

    maximum = len(common_substring[0])

    for element in common_substring:
        if len(element) > maximum:
            maximum = len(element)
            result = element

    return result


str1 = "baseball"
n1 = len(str1)
str2 = "base"
n2 = len(str2)
res = longest_common_substring(str1, str2, n1, n2)
print(res)
