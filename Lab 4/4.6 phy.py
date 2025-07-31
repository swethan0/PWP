def list_to_integer(lst):
    return int(''.join(map(str, lst)))

numbers = [1, 2, 3, 4]
print("Single integer:", list_to_integer(numbers))
