a = int(input("enter th value"))
x = 0
s = 0
pr = 1
while (a > 0):
    t = a
    a = int(a / 10)
    di = t % 10
    s = (s * 10) + di
print("reverse the number",s)