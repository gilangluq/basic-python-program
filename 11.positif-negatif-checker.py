# Function to check if the number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Input from the user
try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Invalid input! Please enter a valid number.")