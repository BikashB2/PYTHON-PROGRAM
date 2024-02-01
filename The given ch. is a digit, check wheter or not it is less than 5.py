a = input("enter the character")
if (a.isdigit()):
    print("the given character is digit")
    b = int(a)
    if (b < 5):
        print("the number is less than 5")
    else:
        print("the number is greater than or equal to 5")
else:
        print("the characteris not a digit")
