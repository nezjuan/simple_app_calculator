class UserInput:
    def ask_user(self, num1, num2, operator):
        operators=["1","2", "3", "4"]
        while True:
            self.operator = input("What operation to use? (numbers only)\n"
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply \n" \
            "4. Divide \n" \
            "CHOICE = ")
            if self.operator in operators:
                break
            else:
                print("Invalid Operator! Please select a valid option")
        self.num1 = float(input("First Number: "))
        self.num2 = float(input("Second Number: "))

class CalculatorFunctions(UserInput):
    def add(self):
        result= self.num1 + self.num2
        print(f"Sum: {self.num1} + {self.num2} = \033[91m{result}\033[0m\n")

    def subtract(self):
        result = self.num1 - self.num2
        print(f"Difference: {self.num1} - {self.num2} = \033[91m{result}\033[0m\n")

    def multiply(self):
        result = self.num1 * self.num2
        print(f"Product: {self.num1} x {self.num2} = \033[91m{result}\033[0m\n")

    def divide(self):
        result = self.num1 / self.num2
        print(f"Quotient: {self.num1} / {self.num2} = \033[91m{result}\033[0m\n")