numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(numbers[::2])

path = "C:\Repositories\test\apple"
path_linux = "/var/repository/test"

sew_windows = "\\"
path_in_tuple = ("c:", "Repositories", "test", "apple")
created_path_win = sew_windows.join(path_in_tuple)

print(created_path_win)

sew_linux = "/"
path_in_tuple = (" ", "Repositories", "test", "apple")
created_path_linux = sew_linux.join(path_in_tuple)

print(created_path_linux)

split_the_win = created_path_win.split(sew_windows)

sew_windows = "\\"
path_in_tuple = ("c:", "Repositories", "test", "apple")
created_path_win = sew_windows.join(path_in_tuple)

print(split_the_win)

text = 'Professor Patryk Walaszkowski is very awesome at teaching Python programming language'
# split the text from space
print(text.split(' '))


