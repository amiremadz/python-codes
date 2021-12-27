from HW4 import Person
from HW4 import Point
from HW4 import Vehicle


############################

teacher = Person("Diane", "Chen")
#print(teacher.last_name)
assert(teacher.last_name == 'Chen')

the_name = teacher.full_name
assert(the_name == 'Diane Chen')

the_name = teacher.name
assert(the_name == 'Chen, Diane')

teacher.first_name = "D. D."
assert(teacher.full_name == 'D. D. Chen')

assert(teacher.name == 'Chen, D. D.')

friend = Person(last_name='McMaster', first_name='Sonia') 
assert(friend.name == 'McMaster, Sonia')

assert(friend.full_name == 'Sonia McMaster')

#########################

point = Point(x=3.25, y=4.5)
 
assert(repr(point) == 'Point(x=3.25, y=4.5)')
 
assert(str(point) == 'Point at (3.25, 4.5)')
 
point
#Point(x=3.25, y=4.5)
 
print(point)
#Point at (3.25, 4.5)

point1 = Point()
assert(point1.magnitude == 0)

#point1
#Point(x=0, y=0)
point2 = Point(y=9)
assert(point2.x == 0)
assert(point2.y == 9)
assert(point2.magnitude == 9)

#point2
#Point(x=0, y=9)

point1 = Point(3, 4)
#point1
#Point(x=3, y=4)
assert(point1.magnitude == 5)

point2 = Point(y=9)
assert(point2.magnitude == 9.0)

print(point2.__repr__())
print(repr(point2))

print(point2.__str__())
print(point2)

#####################

car = Vehicle("Nissan", "Versa", 2018, 25000.5, "Silver")
assert(car.make == 'Nissan')
assert(car.model == 'Versa')
assert(car.year == 2018)
assert(car.price == 25000.5)
assert(car.color == 'Silver')
print(repr(car))
assert(repr(car) == 'Vehicle("Nissan", "Versa", 2018, 25000.50, "Silver")')
#car
#Vehicle("Nissan", "Versa", 2018, 25000.50, "Silver")
assert(str(car) == 'This is a 2018 Silver Nissan Versa costing $25000.50')
print(car)
#This is a 2018 Silver Nissan Versa costing $25000.50
make, model, color = 'Toyota Camry White'.split() # See what I did there? Useful! 
car3 = Vehicle(make, model, 2020, 30000, color)
assert(str(car3) == 'This is a 2020 White Toyota Camry costing $30000.00')
assert(repr(car3) == 'Vehicle("Toyota", "Camry", 2020, 30000.00, "White")')
assert(car3.price ==  30000)

#####################

make, model, color = "Toyota Camry White".split() 
car2 = Vehicle(make, model, 2012, 30010.5, color)
assert(repr(car2) == 'Vehicle("Toyota", "Camry", 2012, 30010.50, "White")')
assert(car2.current_value == 3001.05)
car3 = Vehicle(make, model, 2021, 30010.5, color)
assert(repr(car3) ==  'Vehicle("Toyota", "Camry", 2021, 30010.50, "White")')
assert(car3.current_value == 26259.1875)
car3 = Vehicle(make, model, 2020, 30010.5, color) 
assert(car3.current_value == 22507.875)
car3 = Vehicle(make, model, 2019, 30010.5, color)
assert(car3.current_value == 18756.5625)
car3 = Vehicle(make, model, 2018, 30010.5, color) 
assert(car3.current_value == 15005.25)
car3 = Vehicle(make, model, 2017, 30010.5, color) 
assert(car3.current_value == 11253.9375)
car3 = Vehicle(make, model, 2016, 30010.5, color) 
assert(car3.current_value == 7502.625)
car3 = Vehicle(make, model, 2015, 30010.5, color) 
assert(car3.current_value == 3751.3125)
car3 = Vehicle(make, model, 2014, 30010.5, color)
assert(car3.current_value == 3001.05)
car3 = Vehicle(make, model, 2013, 30010.5, color) 
assert(car3.current_value == 3001.05)
make, model, color = "Toyota Corolla Silver".split()
car4 = Vehicle(make, model, 2016, 20000, color)
assert(repr(car4) == 'Vehicle("Toyota", "Corolla", 2016, 20000.00, "Silver")')
assert(car4.current_value == 5000.0)
car4 = Vehicle(make, model, 2017, 20000, color)
assert(car4.current_value == 7500.0)
car4 = Vehicle(make, model, 2018, 20000, color)
assert(car4.current_value == 10000.0)
car4 = Vehicle(make, model, 2019, 20000, color) 
assert(car4.current_value == 12500.0)
car4 = Vehicle(make, model, 2020, 20000, color) 
assert(car4.current_value == 15000.0)

#######################
make, model, color = "Toyota Camry White".split() 
#car3 = Vehicle(make, model, 201.2, 30000, color) 
#Traceback (most recent call last):
#[...]
#TypeError: Input year must be an integer!
car3 = Vehicle(make, model, 2012, color, color) 
#Traceback (most recent call last):
#[...]
#TypeError: Input price must be a number!


