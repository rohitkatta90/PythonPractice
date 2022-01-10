import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

# Generate a complete random color rather than picking one from the list.

# Here comes the concept of Tuples. Here is how it looks (1, 3, 6) Each of the items that go into a tuple are ORDERED

# Tuples DOES NOT SUPPORT ITEM ASSIGNMENT. Once the tuples are created, they are IMMUTABLE and can never be changed

# If we want to change anything in tuple, then we can put the tuple in the list and then we can change in the list.
