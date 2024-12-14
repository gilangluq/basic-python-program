def find_hcf(x, y):
    """
    Function to find the highest common factor (HCF) or greatest common divisor (GCD) of two numbers.
    Uses the Euclidean algorithm.
    """
    while y:
        x, y = y, x % y
    return x

# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and display the HCF
hcf = find_hcf(num1, num2)
print(f"The Highest Common Factor (HCF) of {num1} and {num2} is {hcf}.")
