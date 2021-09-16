tup = ('developer', 'password', 'database')
lst = ['developer', 'password', 'database']
dikt = {
    'key': 'value',
    'user': 'developer',
    'password': 'admin1234',
    'database': 'MySQL'

}
s = {'developer', 'password', 'database', 'developer'}

print(dikt['password'])
empty = ""
ranges = len(dikt['password'])
for n in range(ranges):
    empty += dikt['password'][ranges - 1 - n]

dikt['password'] = empty
print(dikt['password'])
