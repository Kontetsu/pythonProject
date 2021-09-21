# Exceptions

# Divide smth by zero
a = 1
b = [1, 2, 3, 0, 0, "string", "hello"]
for element in b:
    try:
        print(a / element)
    except (ZeroDivisionError, TypeError) as error:
        print("This is an exception {}".format(error))