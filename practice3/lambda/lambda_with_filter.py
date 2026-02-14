# 1
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 2
greater_than_three = list(filter(lambda x: x > 3, numbers))
print(greater_than_three)


# 3
names = ["Ali", "John", "Anna", "Bob"]
long_names = list(filter(lambda x: len(x) > 3, names))
print(long_names)


# 4
positive = list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2]))
print(positive)


# 5
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)