# simple case of exception handling.
# try:
#     print(5/0)

# except ZeroDivisionError:
#     print("cannot divide by zero.")

# simple division program with exception handling

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

try:
    print(f"Result: {(num1/num2):.2f}")

except ZeroDivisionError:
    print("Division by Zero is not allowed.")