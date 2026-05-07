from calculator_functions import UserInput, CalculatorFunctions
while True:
    print(" * Simple Calculator App * ")

    user = UserInput()
    user.ask_user(Operator=None, Num1=None, Num2=None) 

    if user.operator == "add":
        CalculatorFunctions.add()

    elif user.operator == "subtract":
        CalculatorFunctions.subtract()

    elif user.operator == "multiply":
        CalculatorFunctions.multiply()

    elif user.operator == "divide":
        CalculatorFunctions.divide()
    
    choice=input("Operate more? (Y/N): ")
    if choice != "N":
        print("Thank you for using the application!")
        break