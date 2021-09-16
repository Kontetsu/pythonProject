import sys

total = len(sys.argv) - 1       # because we put 3 args
print("Total number of args {}".format(total))
if total > 2:
    print("Too many arguments")
elif total < 2:
    print("Too less arguments")
elif total == 2:
    print("It's correct")
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    if arg1 > arg2:
        print("Arg 1 is bigger")
    elif arg1 < arg2:
        print("Arg 1 is smaller")
    else:
        print("Arg 1 and 2 are equal!")

# some methods how to check the user input pattern
print("string".isalpha())
print("string1".isalnum())
print("string".isdigit())
print("string".startswith('s'))
print("string".endswith('g'))