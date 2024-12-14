def find_gcd(x, y):
    """
    Helper function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    """
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    """
    Function to find the least common multiple (LCM) of two numbers.
    LCM is calculated using the formula: (x * y) // GCD(x, y)
    """
    return (x * y) // find_gcd(x, y)

# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and display the LCM
lcm = find_lcm(num1, num2)
print(f"The Least Common Multiple (LCM) of {num1} and {num2} is {lcm}.")
