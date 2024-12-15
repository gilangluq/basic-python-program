# Function to perform basic mathematical operations
def simple_calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
    
try:
    print("\nSimple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter an operation (+, -, *, /): ")
    result = simple_calculator(num1, num2, op)
    print(f"Result: {result}")

except ValueError:
    print("Please enter a valid integer or number.")