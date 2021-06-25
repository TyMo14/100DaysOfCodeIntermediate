from turtle import Turtle, Screen
from turtle_shapes import TurtleShape

colours = ["CornFlowerBlue", "SlateGray", "DeepSkyBlue", "LightSeaGreen", "wheat", "pink", "purple"]

turtle = TurtleShape(width=0.1)

# # N-sided shape diagrams
turtle.shapes_overlap(end_n=15)

# Random walk
# turtle.width = 8
# turtle.random_walk(len=(10, 10), steps=100)

# Spirograph
#turtle.spirograph(n=100, radius=150)

screen_obj = Screen()
screen_obj.exitonclick()
