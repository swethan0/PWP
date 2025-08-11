num = int(input("Enter a number: "))
last_digit = num % 10

first_digit = num
while first_digit >= 10:
    first_digit //= 10

print("First digit:", first_digit)
print("Last digit:", last_digit)
