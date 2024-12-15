def convert_number(decimal_number):
    # Convert to binary, octal, and hexadecimal
    binary = bin(decimal_number)[2:]  # Remove the '0b' prefix
    octal = oct(decimal_number)[2:]   # Remove the '0o' prefix
    hexadecimal = hex(decimal_number)[2:].upper()  # Remove the '0x' prefix and make uppercase

    return binary, octal, hexadecimal

# Input from the user
try:
    decimal_number = int(input("Enter a decimal number: "))

    # Get conversions
    binary, octal, hexadecimal = convert_number(decimal_number)

    # Print results
    print(f"Binary: {binary}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")

except ValueError:
    print("Please enter a valid integer.")