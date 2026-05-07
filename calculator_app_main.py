from calculator_functions import UserInput, CalculatorFunctions
while True:
    print(" * Simple Calculator App * ")

    user = UserInput()
    user.ask_user(operator=None, num1=None, num2=None) 

    if user.operator == "add":
        CalculatorFunctions.add(user)

    elif user.operator == "subtract":
        CalculatorFunctions.subtract(user)

    elif user.operator == "multiply":
        CalculatorFunctions.multiply(user)

    elif user.operator == "divide":
        CalculatorFunctions.divide(user)
    
    choice=input("Operate more? (Y/N): ")
    if choice.upper == "N":
        print("Thank you for using the application!")
        break