def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
try:
    number = int(input("Enter a integer(positive): "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}.")
except ValueError:
    print("Please enter a valid integer.")
