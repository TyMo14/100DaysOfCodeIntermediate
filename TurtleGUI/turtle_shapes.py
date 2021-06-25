import turtle as t
import random

t.colormode(255)


class TurtleShape:
    def __init__(self, colour="ForestGreen", shape="turtle", speed="fastest", width=5):
        self.turtle = t.Turtle()
        self.colour = colour
        self.shape = shape
        self.speed = speed
        self.width = width

        self.turtle.shape(shape)
        self.turtle.color(colour)
        self.turtle.pensize(width)
        self.turtle.speed(speed)

    def rgb_tuple(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def random_pen_colour(self, colours=None):
        if colours is None:
            self.turtle.color(self.rgb_tuple())
        else:
            self.turtle.color(random.choice(colours))

    def square(self, len=100) -> object:
        """
        :param len: Length of each side of square

        :return: GUI display of a square
        """
        for i in range(4):
            self.turtle.forward(len)
            self.turtle.right(90)

    def dashed_line(self, num=50, len=10):
        """
        :param n: Number of dashed lines
        :param len: Length of each dash

        :return: GUI display of a dashed line
        """
        for i in range(num):
            self.turtle.pd()
            self.turtle.fd(len)
            self.turtle.pu()
            self.turtle.fd(len)

    def n_side_shape(self, n, len=100):
        """
        :param n: Number of sides in shape being drawn
        :param len: Length of each side

        :return: GUI display of a shape with n-sides
        """

        angle = 360 / n

        for i in range(n):
            self.turtle.fd(len)
            self.turtle.rt(angle)

    def shapes_overlap(self, colours=None, start_n=3, end_n=10):
        """
        :param colours: Input a list of colours otherwise randomly generated
        :param start_n: Number of sides of the first shape drawn
        :param end_n: Number of sides of the last shape drawn

        :return: Overlapping shapes of different sides drawn within each other
        """
        for i in range(start_n, end_n):
            self.random_pen_colour(colours)
            self.n_side_shape(i)

    def change_direction(self, directions=[0, 90, 180, 270]):
        """
        :param directions: Angles that the turtle can change direction in

        :return: New direction for the turtle in the GUI
        """
        self.turtle.setheading(random.choice(directions))

    def random_walk(self, colours=None, len=(10, 50), steps=50):
        """
        :param len: Distance that the turtle can walk in one movement
        :param steps: Number of move that the turtle will make
        :param colours: Colours that the random walk will switch to on each step

        :return: GUI of a turtle moving in same-step increments but the possibility to change direction at every step
        """
        min_len, max_len = len

        for i in range(steps):
            self.random_pen_colour(colours)
            self.change_direction()
            self.turtle.fd(random.randint(min_len, max_len))

    def spirograph(self, radius=100, n=200, colours=None):
        angle = 360/n

        for i in range(n):
            self.random_pen_colour(colours)
            self.turtle.circle(radius)
            self.turtle.left(angle)
