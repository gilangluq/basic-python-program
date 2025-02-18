def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Example usage
num = int(input("Enter a number: "))
if is_happy_number(num):
    print(f"{num} is a Happy Number!")
else:
    print(f"{num} is not a Happy Number.")
