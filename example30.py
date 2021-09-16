# Add any number of numbers
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result


# print(add(1, 2, 3, 4, 5))  # Prints 15


# Prints the name and what the user gives
def print_name_and_something(name, *strings):
    print(f"First name: {name}")
    for string in strings:
        print(string)


print_name_and_something("Bora", "Erget", "Mariol")
