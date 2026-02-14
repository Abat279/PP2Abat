# 1 Simple function without parameters
def greet():
    """Prints a greeting message."""
    print("Hello, World!")

greet()


# 2 Function with one parameter
def greet_user(name):
    """Greets a user by name."""
    print(f"Hello, {name}!")

greet_user("Erkebulan")


# 3 Function performing calculation
def square(number):
    """Prints the square of a number."""
    print(number ** 2)

square(5)


# 4 Function calling another function
def say_goodbye():
    """Prints goodbye message."""
    print("Goodbye!")

def conversation():
    """Simulates a short conversation."""
    greet()
    say_goodbye()

conversation()


# 5 Function with multiple parameters
def add(a, b):
    """Adds two numbers and prints result."""
    print(a + b)

add(10, 20)