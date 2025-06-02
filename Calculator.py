def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Cannot divide by zero."

def calculator():
    while True:
        print("Choose an operation:")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")

        operation = input("Enter your choice (1/2/3/4): ")

        if operation in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid selection")

        another_calculation = input("Would you like to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()