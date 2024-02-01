a = int(input("enter the number"))
if (a < 50):
    print('the no is less than 50')
    if (a > 25):
        print('the number is greater than 25')   
    else:
        print("the number is greater than 25")
    if (a % 2 == 0):
        print("the number is even number")
    else:
        print("the  number is odd number")
else:
        print("the number is greater than or equal to 50 ")