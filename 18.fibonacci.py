def fibonacci_sequence(n):
    """
    Function to print the Fibonacci sequence up to n terms.

    Parameters:
        n (int): Number of terms to print
    """
    # First two terms
    a, b = 0, 1

    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, "term:")
        print(a)
    else:
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=" ")
            # Update values
            a, b = b, a + b

# Input number of terms
num_terms = int(input("Number of terms: "))

# Print Fibonacci sequence
fibonacci_sequence(num_terms)
