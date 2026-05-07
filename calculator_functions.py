class UserInput:
    def ask_user(self, num1, num2, operator):
        self.operator = input("What operation to use? (add, subtract, multiply, divide): ")
        self.num1 = float(input("First Number: "))
        self.num2 = float(input("Second Number: "))

class CalculatorFunctions(UserInput):
    def add(self):
        result= self.num1 + self.num2
        print(f"Sum = {result}")

    def subtract(self):
        result = self.num1 - self.num2
        print(f"Difference = {result}")

    def multiply(self):
        result = self.num1 * self.num2
        print(f"Product = {result}")

    def divide(self):
        result = self.num1 / self.num2
        print(f"Quotient = {result}")