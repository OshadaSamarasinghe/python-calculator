import math

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
    
def square_root(x):
    return math.sqrt(x)

def exponentiation(x, y):
    return x ** y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    'sr': square_root,
    '**': exponentiation,
    'sin': sin,
    'cos': cos,
    'tan': tan
}

history = []

while True:
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (sr)")
    print("6. Exponentiation (**)")
    print("7. Sin (sin)")
    print("8. Cos (cos)")
    print("9. Tan (tan)")
    print("10. Show History")
    print("11. Close")

    choice = input("Enter choice (+/-/*///sr/**/sin/cos/tan/10/11): ")

    if choice == '11':
        print("Bye, See you next time!")
        break

    if choice == '10':
        print("Calculation History:")
        for history_list in history:
            print(history_list)
            
        continue

    if choice in operations:
        if choice in ('sr','sin','cos','tan'):
            num = float(input("Enter a number: "))
            result = operations [choice] (num)
            calculation = f"{choice}{num} = {result}"
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = operations[choice](num1, num2)
            calculation = f"{num1} {choice} {num2} = {result}"
        
        history.append(calculation)
        print("Result:", calculation)
        print(" ")
    else:
        print("Invalid input")
