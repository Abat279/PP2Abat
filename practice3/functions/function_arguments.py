# 1 Positional arguments
def subtract(a, b):
    """Subtracts b from a."""
    print(a - b)

subtract(10, 3)


# 2 Default argument
def power(base, exponent=2):
    """Raises base to exponent power."""
    print(base ** exponent)

power(5)
power(5, 3)


# 3 Keyword arguments
def student_info(name, age):
    """Prints student info."""
    print(f"Name: {name}, Age: {age}")

student_info(age=17, name="Ali")


# 4 Mixed arguments
def introduce(name, country="Kazakhstan"):
    """Introduces a person."""
    print(f"{name} is from {country}")

introduce("Erkebulan")
introduce("John", "USA")


# 5 Passing list as argument
def print_list(items):
    """Prints each item in a list."""
    for item in items:
        print(item)

print_list(["apple", "banana", "cherry"])