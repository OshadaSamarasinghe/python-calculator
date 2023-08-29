def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Can't divide by zero"

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

history = []

while True:
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Show History")
    print("6. Close")

    choice = input("Enter choice (+/-/*///5/6): ")

    if choice == '6':
        print("Bye, See you next time!")
        break

    if choice == '5':
        print("Calculation History:")
        for history_list in history:
            print(history_list)
            
        continue

    if choice in operations:
        operator = operations[choice]
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = operator(num1, num2)
        calculation = f"{num1} {choice} {num2} = {result}"
        history.append(calculation)
        print("Result:", calculation)
        print(" ")
    else:
        print("Invalid input")
