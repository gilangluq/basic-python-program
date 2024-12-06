# Python program to solve a quadratic equation 
import math

def quadratic_solver(a, b, c):
    # Check if it's a valid quadratic equation
    if a == 0:
        return "Coefficient 'a' cannot be 0 for a quadratic equation."
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The roots are real and distinct: {root1} and {root2}"
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return f"The roots are real and the same: {root}"
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (f"The roots are complex: "
                f"{real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = quadratic_solver(a, b, c)
print(result)