from calculator_functions import UserInput, CalculatorFunctions
while True:
    print(" * Simple Calculator App * ")

    UserInput() 

    if UserInput.operator == "add":
        CalculatorFunctions.add()

    elif UserInput.operator == "subtract":
        CalculatorFunctions.subtract()

    elif UserInput.operator == "multiply":
        CalculatorFunctions.multiply()

    elif UserInput.operator == "divide":
        CalculatorFunctions.divide()
    
    choice=input("Operate more? (Y/N): ")
    if choice != "N":
        print("Thank you for using the application!")
        break