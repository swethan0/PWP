def count_digits(num):
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count

number = int(input("Enter a number: "))
print("Number of digits:", count_digits(number))
