def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    return a / b
 
def modulus(a, b):
    return a % b
 
 
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /, %): ")
 
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    elif op == "%":
        result = modulus(num1, num2)
    else:
        result = "Invalid operation"
 
    print("Result:", result)
 
    again = input("Do you want another calculation? (yes/no): ")
    if again == "no":
        print("Goodbye!")
        break
