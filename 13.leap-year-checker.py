def is_leap_year(year):
    """
    Function to check if a year is a leap year.
    A year is a leap year if:
    - It is divisible by 4, and
    - Not divisible by 100 unless it is also divisible by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Input from the user
year = int(input("Enter a year to check if it is a leap year: "))

# Check and display the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
