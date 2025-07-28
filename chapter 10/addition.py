# One common problem when prompting for numerical input occurs when people
# provide text instead of numbers. When you try to convert the input to an int,
# you’ll get a ValueError. Write a program that prompts for two numbers.
# Add them together and print the result. Catch the ValueError if either input
# value is not a number, and print a friendly error message. Test your program
# by entering two numbers and then by entering some text instead of a number.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    result = int(num1) + int(num2)

except ValueError:
    print("Please enter valid numerical values to add.")

else:
    print(f"{num1} + {num2} = {result}")