while True:
    print(" * Simple Calculator App * ")

    operator = input("What operation to use? (add, subtract, multiply, divide): ")
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: ")) 

    def add():
        result= num1 + num2
        print(f"Sum = {result}")

    def subtract():
        result = num1 - num2
        print(f"Difference = {result}")

    def multiply():
        result = num1 * num2
        print(f"Product = {result}")

    def divide():
        result = num1 / num2
        print(f"Quotient = {result}")

    if operator == "add":
        add()

    elif operator == "subtract":
        subtract()

    elif operator == "multiply":
        multiply()

    elif operator == "divide":
        divide()
    
    choice=input("Operate more? (Y/N): ")
    if choice != "N":
        print("Thank you for using the application!")
        break