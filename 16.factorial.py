# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            factorial = factorial*1
        return factorial

# Input from the user
number = int(input("Enter a number: "))

# Check if the input is a non-negative integer
if number < 0:
    print("Factorial does not exist for negative numbers")
else:
    # Calling the factorial function
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
