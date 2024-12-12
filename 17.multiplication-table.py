# Program to display the multiplication table

def display_multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Input from user
try:
    num = int(input("Enter the number for the multiplication table: "))
    up_to = int(input("Enter the range up to which you want the table (default is 10): ") or 10)
    display_multiplication_table(num, up_to)
except ValueError:
    print("Please enter a valid number.")