def is_armstrong(number):
    # Convert the number to a string to easily iterate through its digits
    digits = str(number)
    # Calculate the number of digits (order)
    num_digits = len(digits)
    # Compute the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    # Check if the calculated sum matches the original number
    return armstrong_sum == number

# Input from the user
number = int(input("Enter a number: "))

# Check and display the result
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")