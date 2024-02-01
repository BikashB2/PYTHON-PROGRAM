matrix = [[1, 2], [2, 3], [3, 4]]

transpose = map(list, zip(*matrix))

for i in transpose:
    print(i)