def CountWords():
    words = input("Hey!! What's on your mind today??\n")

    result = words.split()
    Number = len(words.split())
    #print(result)
    print("You used",Number ,"words to tell me what's on your mind.")
    return " "



print(CountWords())
