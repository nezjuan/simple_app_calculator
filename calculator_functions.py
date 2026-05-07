class UserInput:
    def ask_user(self, num1, num2, operator):
        self.num1=num1
        self.num2=num2
        self.operator=operator

        operator = input("What operation to use? (add, subtract, multiply, divide): ")
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))

class CalculatorFunctions(UserInput):
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