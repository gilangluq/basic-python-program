def is_prime(number):
    """
    Function to check if a number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Input interval from the user
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print(f"Prime numbers between {start} and {end} are:")

# Find and print all prime numbers in the interval
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
