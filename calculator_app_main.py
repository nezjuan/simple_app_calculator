print(" * Simple Calculator App * ")

operator = input("What operation to use? (add, subtract, multiply, divide): ").lower
num1 = float(input("First Number: "))
num2 = float(input("Second Number: ")) 

if operator == "add":
    result = num1 + num2
    print(f"Sum = {result}")

elif operator == "subtract":
    result = num1 - num2
    print(f"Difference = {result}") 

elif operator == "multiply":
    result = num1 * num2
    print(f"Product = {result}")

elif operator == "divide":
    result = num1 / num2
    print(f"Quotient = {result}")