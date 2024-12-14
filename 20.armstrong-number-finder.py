def is_armstrong(number):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    """
    # Convert the number to a string to extract digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return armstrong_sum == number

def find_armstrong_numbers(start, end):
    """
    Find all Armstrong numbers in the interval [start, end].
    """
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Input: Start and End of the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Find Armstrong numbers in the interval
armstrong_numbers = find_armstrong_numbers(start, end)

# Display the results
if armstrong_numbers:
    print(f"Armstrong numbers in the interval [{start}, {end}]: {armstrong_numbers}")
else:
    print(f"No Armstrong numbers found in the interval [{start}, {end}].")
