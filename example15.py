# C:\Repositories\test\apple
# /Repositories/test/apple

path1 = "C:\Repositories\\test\\apple"
path1 = path1.replace('e', 'a')

print(path1)

path_to_strip = "C:\      Repositories      \           test      \      apple"

path = "".join(path_to_strip.split())
print(path)

path2 = path_to_strip.replace(" ", "")
print(path2)