def largest(*args):
    if len(args) == 0:
        return None
    largest_num = args[0]
    for num in args:
        if num > largest_num:
            largest_num = num
    return largest_num

# Example usage
numbers = [10, 5, 20, 15, 25]
result = largest(*numbers)
print("The largest number is:", result)
