from calculator_functions import UserInput, CalculatorFunctions
print(" * Simple Calculator App * \n")
while True:

    try:
        user = UserInput()
        user.ask_user(operator=None, num1=None, num2=None) 

        if user.operator == "1":
            CalculatorFunctions.add(user)

        elif user.operator == "2":
            CalculatorFunctions.subtract(user)

        elif user.operator == "3":
            CalculatorFunctions.multiply(user)

        elif user.operator == "4":
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