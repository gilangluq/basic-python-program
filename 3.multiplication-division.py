# Multiplication & Division

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

mul = num1 * num2
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div = num1 / num2
print(f"Multiplication: {num1} x {num2} = {mul}")
print(f"Division: {num1} / {num2} = {div}")
