def is_prime(number):
    """
    Function to check if a number is a prime number.
    A number is prime if it is greater than 1 and has no divisors other than 1 and itself.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter a number to check if it is prime: "))

# Check and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")