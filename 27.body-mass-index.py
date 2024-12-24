def calculate_bmi(weight, height):
    """Function to calculate BMI given weight in kg and height in meters."""
    return weight / (height ** 2)

def bmi_category(bmi):
    """Determine BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Prompt user for input
try:
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in centimeters (cm): "))
    
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
except ValueError:
    print("Please enter valid numerical inputs for weight and height.")
