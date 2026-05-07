class UserInput:
    def ask_user(self, num1, num2, operator):
        operators=["1","2", "3", "4"]
        while True:
            self.operator = input("What operation would you want to use? (numbers only)\n"
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

class SaveHistory:
    def save_history(self, operation, num1, num2, result):
        with open("history.txt", "a") as math_history:
            math_history.write(f"{operation.upper()}: {num1} {operation} {num2} = {result}\n")

class CalculatorFunctions(UserInput, SaveHistory):
    def add(self):
        result= self.num1 + self.num2
        print(f"Sum: {self.num1} + {self.num2} = \033[92m{result}\033[0m\n")
        self.save_history("add", self.num1, self.num2, result)
        return result
        
    def subtract(self):
        result = self.num1 - self.num2
        print(f"Difference: {self.num1} - {self.num2} = \033[92m{result}\033[0m\n")
        self.save_history("subtract", self.num1, self.num2, result)
        return result

    def multiply(self):
        result = self.num1 * self.num2
        print(f"Product: {self.num1} x {self.num2} = \033[92m{result}\033[0m\n")
        self.save_history("multiply", self.num1, self.num2, result)
        return result

    def divide(self):
        result = self.num1 / self.num2
        print(f"Quotient: {self.num1} / {self.num2} = \033[92m{result}\033[0m\n")
        self.save_history("divide", self.num1, self.num2, result)
        return result