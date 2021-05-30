def Percentage(e,m,s,soc,h):

    if e<=100 and m<=100 and s<=100 and soc<=100 and h<=100:
        percentage = ((e + m + s + soc + h) / 500) * 100
        return percentage

    else:
        print("Marks should be less than or equal to 100.")
        return ""


e = float(input("Enter the marks of English:\n"))
m = float(input("Enter the marks of Mathematics:\n"))
s = float(input("Enter the marks of Science:\n"))
soc = float(input("Enter the marks of Social Science:\n"))
h = float(input("Enter the marks of Hindi:\n"))



print(Percentage(e,m,s,soc,h))
