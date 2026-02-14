# 1
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)


# 2
sorted_desc = sorted(numbers, key=lambda x: -x)
print(sorted_desc)


# 3
names = ["Ali", "John", "Bob"]
sorted_by_length = sorted(names, key=lambda x: len(x))
print(sorted_by_length)


# 4
students = [("Ali", 90), ("John", 85), ("Anna", 95)]
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)


# 5
words = ["apple", "banana", "cherry"]
sorted_last_letter = sorted(words, key=lambda x: x[-1])
print(sorted_last_letter)