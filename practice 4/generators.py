# generators.py

# 1. Iterator with list
a = [1, 2, 3]
it = iter(a)
print(next(it))
print(next(it))
print(next(it))

# 2. Iterator with string
s = "ABC"
it2 = iter(s)
print(next(it2))
print(next(it2))

# 3. Simple generator
def gen1():
    yield 1
    yield 2
    yield 3

for x in gen1():
    print(x)

# 4. Generator with loop
def gen2():
    for i in range(5):
        yield i

for x in gen2():
    print(x)

# 5. Generator expression
sq = (x*x for x in range(4))
for x in sq:
    print(x)