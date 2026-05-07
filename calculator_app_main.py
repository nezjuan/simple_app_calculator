from calculator_functions import UserInput, CalculatorFunctions
while True:
    print(" * Simple Calculator App * ")

    try:
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

    except ZeroDivisionError:
        print("You Can't Divide by Zero 0!")
    except ValueError:
        print("Numbers Only Please!")
    except Exception:
        print("Something Went Wrong!")

    while True:
        choice=input("Operate more? (Y/N): ")
        if choice.upper() == "N":
            print("Thank you for using the application!")
            exit()
        elif choice.upper() == "Y":
            break
        else:
            print("Invalid Input!")