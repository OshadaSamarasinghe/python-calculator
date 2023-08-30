import math

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Can't divide by zero"
    
def square_root(n1):
    return math.sqrt(n1)

def exponentiation(n1, n2):
    return n1 ** n2

def sin(n1):
    return math.sin(math.radians(n1))

def cos(n1):
    return math.cos(math.radians(n1))

def tan(n1):
    return math.tan(math.radians(n1))

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
    print("10. Close")

    choice = input("Enter choice (+/-/*///sr/**/sin/cos/tan/10): ")

    if choice == '10':
        print("Bye, See you next time!")
        break

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

        print("Result:", calculation)
        print(" ")
    else:
        print("Invalid input")
