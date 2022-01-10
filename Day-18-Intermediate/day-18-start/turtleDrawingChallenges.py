import random
from turtle import *

# Challenge one
tim = Turtle()

# for _ in range(15):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
#
# screen = Screen()
# screen.exitonclick()

# Challenge 2:


# Approach - 1 (My way)

# Drawing a triangle
# tim.color("red")
#
# for line in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# # Drawing a square
# tim.color("green")
# for line in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# # Drawing a pentagon
# tim.color("orange")
# for line in range(5):
#     tim.forward(100)
#     tim.right(72)
#
#
# # Draw a hexagon
# tim.color("purple")
# for line in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# # Draw a heptagon
# tim.color("pink")
# for line in range(7):
#     tim.forward(100)
#     tim.right(51.43)
#
# # Draw a octagon
# tim.color("indigo")
# for line in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# # Draw a nonagon
# tim.color("cyan")
# for line in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# # Draw a decogon
# tim.color("blue")
# for line in range(10):
#     tim.forward(100)
#     tim.right(36)
#
# screen = Screen()
# screen.exitonclick()


# Approach 2 - Angela's way

colors = ["blue", "aquamarine", "lime green", "gold", "peru", "firebrick", "pink", "medium violet red", "blue violet"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for line in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    random_color = random.choice(colors)
    tim.color(random_color)
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()


