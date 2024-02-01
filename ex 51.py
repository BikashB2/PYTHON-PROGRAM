def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
no1 = int(input("enter the 1st number"))
no2 = int(input("enter the 2nd number"))
no3 = int(input("enter the 3nd number"))
result = maximum(no1, no2, no3)
print("maximum number between three no. is",result)
 