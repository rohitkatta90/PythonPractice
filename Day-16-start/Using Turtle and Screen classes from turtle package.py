from turtle import Turtle, Screen

# Turtle() is the Class, timmy is the object of the Class Turtle. This is the syntax of creating object
timmy = Turtle()
print("Printing object")
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()
