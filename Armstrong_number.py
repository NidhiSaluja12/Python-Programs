number = int(input("Enter the number to br checked:\n"))
order = len(str(number))                                         # Number of digits in the number
sum = 0



copy_of_number = number                                          # num will become 0 after while loop so copy should be made
while (number > 0):
    digits = number % 10                                         # 153%10 = 3 ; 15%10 = 5 ; 1%10 = 1
    sum += digits ** order                                       # 1*1*1 + 5*5*5 + 3*3*3
    number = number // 10                                        # 153//10=15 ; 15//10=1 ; 1//10=0
if (sum == copy_of_number):
    print(f"{copy_of_number} is an armstrong number")

else:
    print(f"{copy_of_number} is not an armstrong number")
