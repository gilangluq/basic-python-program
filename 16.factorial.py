def list_factorials(n):
    """Returns a list of factorial numbers up to the given number n."""
    factorials = []
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        factorials.append(factorial)
    return factorials

# Get user input
try:
    user_input = int(input("Enter a positive integer: "))
    if user_input < 0:
        print("Please enter a non-negative integer.")
    else:
        result = list_factorials(user_input)
        print(f"Factorial numbers up to {user_input}: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
