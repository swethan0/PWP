num = input("Enter a number: ")

if len(num) <= 1:
    swapped = num
else:
    swapped = num[-1] + num[1:-1] + num[0]

print("Swapped number:", swapped)
