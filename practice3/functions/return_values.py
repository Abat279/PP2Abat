# 1 Returning a value
def multiply(a, b):
    """Returns multiplication result."""
    return a * b

result = multiply(4, 5)
print(result)


# 2 Returning multiple values
def min_max(numbers):
    """Returns minimum and maximum from list."""
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9])
print(minimum, maximum)


# 3 Early return
def check_even(number):
    """Returns True if number is even."""
    if number % 2 == 0:
        return True
    return False

print(check_even(8))


# 4 Returning string
def full_name(first, last):
    """Returns full name."""
    return f"{first} {last}"

print(full_name("Erkebulan", "Smith"))


# 5 Returning dictionary
def create_student(name, grade):
    """Returns student dictionary."""
    return {"name": name, "grade": grade}

print(create_student("Ali", 90))