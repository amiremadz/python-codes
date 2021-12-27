"""Python Fundamentals Final Project - shapes module."""
# Please Put Your Name Here
import math

class Point:
    """Two-Dimensional Point(x, y)"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point at ({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

    def __iter__(self):
        yield self.x
        yield self.y

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def loc_from_tuple(self, coords):
        self.x, self.y = coords
        return self

    @classmethod
    def from_tuple(cls, coords):
        x, y = coords
        return cls(x, y)

class Circle:
    """Circle(center, radius) where center is a Point instance"""
    def __init__(self, center=Point(), radius=1):
        self.center = center
        self.radius = radius
        if radius < 0:
            raise ValueError("radius cannot be negative")
        if not isinstance(center, Point()):
            raise ValueError("the center of the circle should be a Point")

    def __str__(self):
        return "Circle with center at {} and radius {}".format(self.center, self.radius)

    def __repr__(self):
        return "Circle(center={}, radius=1.5)".format(self.center, self.radius)

    @property
    def radius(self):
        return self.radius

    @property
    def diameter(self):
        return self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2





