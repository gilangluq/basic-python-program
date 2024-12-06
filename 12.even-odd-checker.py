def check_odd_even(num):
    if num % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Input from the user
try:
    number = int(input("Enter an integer: "))
    result = check_odd_even(number)
    print(result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")