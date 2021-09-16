# def printing_arg(arg1, arg2):
#     print(arg1)
#     print(arg2)
#
#
# def add_values(arg1, arg2):
#     result = arg1 + arg2
#     print(result)
#
#
# def print_user_input():
#     user_input = input("Enter an input: ")
#     print("user input is {}".format(user_input))
# Imports

# Classes definitions
# Function definitions
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
        return arg1 / arg2
    else:
        print("Incorrect operation")
        exit()


def printing_arguments(arg1, arg2):
    print(arg1)
    print(arg2)


def print_user_input():
    user_input = input("Put a value here: ")
    print("User input is: {}".format(user_input))



def main():
    first = int(input("Plese enter the values:"))
    second = int(input("Plese enter the values:"))
    op = input("Plese enter the values:")
    x = resolve_equation(first, second, op)
    print(x)
    y = resolve_equation(first, second, op)
    print(y)
    # y = resolve_equation(x, 6, "*")
    # print(y)


# Execution
if __name__ == "__main__":
    main()

def main():
    print("Hello World!")
    # a = "test1"
    # b = "test2"
    # printing_arg(1, 2)
    # printing_arg(a, b)


# if __name__ == "__main__":
#     main()
#     # print_user_input()
#     main()
#     # print_user_input()
#     # add_values(8, 5)
