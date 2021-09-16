# Variables
var1 = "Variable one"
var2 = "variable two"


def resolve_equation(arg1, arg2, operator):
    if operator == "+":
        print("Adding")
        return arg1 + arg2
    elif operator == "-":
        print("Substract")
        return arg1 - arg2
    elif operator == "*":
        print("Multiply")
        return arg1 * arg2
    elif operator == "/":
        print("Division")
        return arg1 - arg2
    else:
        print("Incorrect operation")
        exit()
