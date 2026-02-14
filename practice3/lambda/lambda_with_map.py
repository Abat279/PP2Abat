# 1
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


# 2
names = ["ali", "john", "anna"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)


# 3
lengths = list(map(lambda x: len(x), names))
print(lengths)


# 4
double = list(map(lambda x: x * 2, numbers))
print(double)


# 5
prices = [100, 200, 300]
with_tax = list(map(lambda x: x * 1.1, prices))
print(with_tax)