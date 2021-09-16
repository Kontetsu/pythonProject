
print(range(10))

print(range(5, 10))

print(range(5, 20, 2))

seq = range(1)
for var in seq:
    print(var)

long_string = "Lorem Ipsum is simply dummy text of the printing and typesetting" \
              " industry. Lorem Ipsum has been the industry's standard dummy text" \
              " ever since the 1500s, when an unknown printer took a galley of type" \
              " and scrambled it to make a type specimen book. "
print(len(long_string))
for c in range(11):
    print(long_string[c])

long_list = long_string.split()
print(long_string.split())
for c in range(11):
    print(long_list[c])