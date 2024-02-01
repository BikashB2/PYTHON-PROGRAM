a = int(input("enter the value"))
x = 0
while (a > 0):
    a = int(a / 10)
    x = x + 1
    print("no of digit:",x)