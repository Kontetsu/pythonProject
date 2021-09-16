user_input = int(input("Please put the number: "))
while True:
    # user_input -= user_input        # user_input = user_input - 1
    print("Actual value = {}".format(user_input))
    user_input = user_input - 1
    if user_input == 0:
        print("User input = {}".format(user_input))
        break         # breaking the loop
print("Outside loop")