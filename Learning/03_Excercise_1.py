# Calculator

a = int(input("Enter First Number: ").strip())
operator = input("Enter the Operator: ").strip()
b = int(input("Enter Second Number: ").strip())


if operator == "/":
    print(f"Divsion of Numbers is: {a/b}")
elif operator == "+":
    print(f"Addition of Numbers is: {a+b}")
elif operator == "-":
    print(f"substraction of numbers is: {a-b}")
else:
    print(f"Multiplication of numbers is: {a*b}")