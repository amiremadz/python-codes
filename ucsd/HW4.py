"""Homework 4 for CSE-41273"""
# Replace this with your name
import datetime
import math


# Part 1
class Person:
    """Person with first and last name."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def name(self):
        return self.last_name + ', ' + self.first_name

# Part 2
class Point:
    """2-D Point objects."""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x,self.y)

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)



# Part 3
class Vehicle:
    """A simple class representing a vehicle"""
    def __init__(self, car_make, car_model, car_year, car_price, car_color):
        self.car_make = car_make
        self.car_model = car_model 
        
        if isinstance(car_year, int):
            self.car_year = car_year
        else:
            raise TypeError('Input year must be an integer!')

        if isinstance(car_price, int) or isinstance(car_price, float):
            self.car_price = car_price
        else:
            raise TypeError('Input price must be a number!')

        self.car_color = car_color
        
    @property
    def make(self):
        return self.car_make

    @property
    def model(self):
        return self.car_model
    
    @property
    def year(self):
        return self.car_year

    @property
    def price (self):
        return self.car_price
    
    @property
    def color (self):
        return self.car_color

    
    @property
    def current_year(self):
        """Return the current year"""
        return datetime.datetime.now().year
    
    @property
    def current_value(self):
        car_age = self.current_year - self.car_year + 1
        if car_age > 7:
            car_value = self.car_price*0.1
        elif car_age <= 7:
            car_value = self.car_price - (self.car_price * 0.125) * (self.current_year - self.car_year + 1)
        
        return car_value
    
    def __repr__(self):
        return 'Vehicle("{}", "{}", {}, {:.2f}, "{}")'.format(self.car_make, self.car_model, self.car_year, self.car_price, self.car_color)

    def __str__(self):
        return 'This is a {} {} {} {} costing ${:.2f}'.format(self.car_year, self.car_color, self.car_make, self.car_model, self.car_price)
    

    
    
