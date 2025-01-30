class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


print("Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

operation = int(input("Choose an operation (1/2/3/4): "))
if operation != (1,2,4,3):
    print("corrent number")
else:
   
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

calculator = Calculator()

if operation == 1:
    print(f"Result: {calculator.add(num1, num2)}")
elif operation == 2:
    print(f"Result: {calculator.subtract(num1, num2)}")
elif operation == 3:
    print(f"Result: {calculator.multiply(num1, num2)}")
elif operation == 4:
    print(f"Result: {calculator.divide(num1, num2)}")
