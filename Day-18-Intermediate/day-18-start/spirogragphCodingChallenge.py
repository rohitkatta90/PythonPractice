import turtle
import random

tim = turtle.Turtle()
# tim.position()
tim.speed("fastest")

# My approach
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
# for _ in range(36):
#     tim.color(random.choice(colours))
#     tim.circle(100)
#     tim.left(10)
#
# screen = Screen()
# screen.exitonclick()

# Angela's Approach

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(20)
