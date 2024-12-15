# Function to find ASCII value of a character
def find_ascii_value(character):
    return ord(character)

# Input from the user
char = input("Enter a character to find its ASCII value: ")

if len(char) == 1:
    # Get the ASCII value
    ascii_value = find_ascii_value(char)
    print(f"ASCII value of '{char}': {ascii_value}")
else:
    print("Please enter a single character.")
