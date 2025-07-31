def get_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

numbers = [1, 2, 2, 3, 3, 3, 4]
print("Frequency of elements:", get_frequency(numbers))
