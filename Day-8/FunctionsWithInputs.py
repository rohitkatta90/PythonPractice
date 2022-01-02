# Functions with Inputs

# SYNTAX

# def my_function(something):
#     print("Hello")
#     #Do this with something
#     # Then do this 
#     # Finally do this

# my_function(123)

# SO IN ABOVE EXAMPLE, "something" is called PARAMETER and in function call "123" is called ARGUMENT


# Simple Function
# def greet():
#     print("Hello")
#     print("How are you doing?")

# greet()

# Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Rohit")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

# This is the example of Positional Arguments
greet_with("Rohit", "New York")

# This is the example of Keyword Arguments
greet_with(location="Seattle", name="Rohit")