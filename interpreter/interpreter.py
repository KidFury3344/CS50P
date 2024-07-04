expression = input("Expression: ")

if expression.find("+") != -1:
    num1 = int(expression[:expression.find("+")].strip())
    num2 = int(expression[expression.find("+")+1:].strip())
    result = float(num1 + num2)
if expression.find("-") != -1:
    num1 = int(expression[:expression.find("-")].strip())
    num2 = int(expression[expression.find("-")+1:].strip())
    result = float(num1 - num2)
if expression.find("*") != -1:
    num1 = int(expression[:expression.find("*")].strip())
    num2 = int(expression[expression.find("*")+1:].strip())
    result = float(num1 * num2)
if expression.find("/") != -1:
    num1 = int(expression[:expression.find("/")].strip())
    num2 = int(expression[expression.find("/")+1:].strip())
    result = float(num1 / num2)


print(result)