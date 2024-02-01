
t = (1, 2, 3, 3, 4)
result = []
for item in t:
    if item not in result:
        result.append(item)
t = tuple(result)
print(t)