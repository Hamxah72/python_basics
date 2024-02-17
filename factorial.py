# Read the number from user
number = int(input("Enter a number: "))

# Initialize variables
counter = 1
factorial = 1

# Loop until counter reaches the input number
while counter <= number:
    # Multiply current value of counter with factorial
    factorial *= counter
    # Increment counter by 1
    counter += 1

# Print the factorial of the number
print("Factorial of", number, "is", factorial)
