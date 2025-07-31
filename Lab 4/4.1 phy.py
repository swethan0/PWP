def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [2, 3, 4]
print("Product of list items:", multiply_list(numbers))
