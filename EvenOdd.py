def EvenOdd():

    num = int(input())

    if num==0:
        print("The number is neither even nor odd. Any other ?")

    elif num%2==0:
        print("That's an even number. Any other number?")

    else:
        print("That's an odd number. Any other number?")

    return " "

print("What number are you thinking?")
print(EvenOdd())
print(EvenOdd())
