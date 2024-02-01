a = int(input("enter the value"))
x = 0
s = 0
pr = 1
while (a > 0):
    t = a
    a = int(a / 10)
    di = t % 10
    s = s + di
    pr = pr * di
    print("sum of digit", s)
    print("product of digits:",pr)