#  1 args example
def sum_all(*numbers):
    """Sums all given numbers."""
    print(sum(numbers))

sum_all(1, 2, 3, 4)


#  2 args with loop
def print_numbers(*numbers):
    """Prints each number."""
    for num in numbers:
        print(num)

print_numbers(5, 10, 15)


#  3 kwargs example
def print_info(**info):
    """Prints key-value pairs."""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Erkebulan", age=17)


#  4 Combined *args and **kwargs
def mixed_example(*args, **kwargs):
    """Prints args and kwargs."""
    print("Args:", args)
    print("Kwargs:", kwargs)

mixed_example(1, 2, name="Ali")


#  5 Using *args in calculation
def multiply_all(*numbers):
    """Multiplies all numbers."""
    result = 1
    for num in numbers:
        result *= num
    print(result)

multiply_all(2, 3, 4)