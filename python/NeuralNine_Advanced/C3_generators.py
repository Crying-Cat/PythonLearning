def mygenerator(n):
    for x in range(n):
        yield x

values = mygenerator(200)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

for i in mygenerator(200):
    print(i)
