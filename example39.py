import os
import random
import datetime

x = random.randint(0, 1024)
name = "example_file_{}.txt".format(x)
print(name)
print(datetime.datetime.now())

# Check that file name is existing in returned list
if name in os.listdir():
    print("Existing!")

# Writing to file (appending)
with open(name, 'a') as f:
    # file_name        mode (append)
    for n in range(1024):
        f.write("Line {}\n".format(n))

# Read the file
with open(name, 'r') as f:
    print(f.read())

# Overwrite the file (w - overwriting the file)!!!
# with open(name, 'w') as f:
#     f.write("Third Line\n")
#     f.write("Fourth line\n")

# Read the file
with open(name, 'r') as f:
    print(f.read())

# os.remove(name)
if name not in os.listdir():
    print("Removed!")