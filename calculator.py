#Define variables
value1 = input("Input a number: ")
function = str(input("Input a function: (+, -, *, or /): "))
value2 = input("Input a second number: ")

#Convert strings to numbers
num1 = float(value1)
num2 = float(value2)

#Define functions
def add(num1, num2):
    return num1 + num2
def multiply(num1, num2):
    return value1 * value2
def subtract(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1 / num2

#Execute math
def math(num1, num2, function):
	if function in ["+"]:
		return print(add(num1, num2))
	elif function in ["-"]:
		return print(subtract(num1, num2))
	elif function in ["*"]:
		return print(multiply(num1, num2))
	elif function in ["/"]:
		return print(divide(num1, num2))
	else:
		return print("Invalid function input")

math(num1, num2, function)
