# Swap two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")

# Display the original values
print(f"Original values: a = {a}, b = {b}")

# Swap the values using temporary variable
temp = a
a = b
b = temp

# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")

# Swap the values without using temporary variable
a, b = b, a

# Display the swapped values
print(f"Re-Swapped values: a = {a}, b = {b}")
