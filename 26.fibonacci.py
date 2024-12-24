def fibonacci(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def display_fibonacci_sequence(length):
    """Function to display the Fibonacci sequence up to the given length."""
    if length <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(length):
            print(fibonacci(i), end=" ")

# Prompt user for the number of terms
try:
    num_terms = int(input("Enter the number of terms: "))
    display_fibonacci_sequence(num_terms)
except ValueError:
    print("Please enter a valid integer.")
