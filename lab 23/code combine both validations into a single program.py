import re

def validate_pan(pan):
    pan = pan.strip().upper()
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.fullmatch(pattern, pan))

def validate_email(email):
    email = email.strip()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))

pan = input("Enter PAN card number: ")
email = input("Enter Email ID: ")

print("\n-- Validation Results ---")

if validate_pan(pan):
    print("PAN Card: Valid")
else:
    print("PAN Card: Invalid. Format: ABCDE1234F")

if validate_email(email):
    print("Email ID: Valid")
else:
    print("Email ID: Invalid. Format: user@example.com")
