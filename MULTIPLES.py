multiples_of_17 = []

for num in range(2000, 2501):
    if num % 17 == 0 and num % 5 != 0:
        multiples_of_17.append(num)

print("Multiples of 17, but not multiples of 5:")
print(multiples_of_17)
