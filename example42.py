import os
import random

# Execute a command
os.system('echo "Test"')

# Setting env variable:
# linux/unix/macos -> export VARIABLE=PATH
# windows -> SET TEST="Name"

os.environ['USER'] = 'patryk.walaszkowski'
os.environ['PASSWORD'] = 'admin1234'

# Print env variables
# linux -> $TEST
# windows -> echo %TEST%

print(os.getenv("USER"))
print(os.getenv("PASSWORD"))

# Paths
create_a_path = os.path.join("C:\\", "Repositories", "LH1AL_prod", "simple_file_parser")
relative = os.path.join("simple_file_parser")
print("Generated path {}".format(create_a_path))
print("My CWD {}".format(os.getcwd()))

# os.chdir(relative)
# print("My CWD {}".format(os.getcwd()))

# path = "C:\Repositories\test\apple"
# path_linux = "/Repositories/test/apple"
#
# sep_windows = "\\"
# path_in_tuple = ("C:", "Repositories", "test", "apple")
# created_path_win = sep_windows.join(path_in_tuple)
# print(created_path_win)
#
# sep_linux = "/"
# path_in_tuple_lin = ("","Repositories", "test", "apple")
# created_path_lin = sep_linux.join(path_in_tuple_lin)
# print(created_path_lin)

x = random.randint(0, 1024)
random_name = "example_file_{}".format(x)
# os.mkdir(random_name)       # Working directory (from where script is executed)

test_path = os.path.join("sample_file_parser", "test")
path_to_replace = os.path.join("sample_file_parser", "changed_test")
# Check that directory is not existing:
if not os.path.exists(test_path):
    os.mkdir(test_path)

# If below list is empty then the whole stuff is empty
print(os.listdir(test_path))

os.rename(test_path, path_to_replace)
