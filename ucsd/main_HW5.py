from HW5 import Circle
from HW5 import BankAccount

circle = Circle()
assert(repr(circle) == 'Circle(radius=1)')
# repr(circle)
# 'Circle(radius=1)'
print(circle)
assert(str(circle) ==  'Circle with radius of 1')
assert(type(circle.history) == list)
assert(circle.history[0] == 1)
circle.radius = 2
circle.diameter = 3 
assert( circle.radius == 1.5)

gt = [1, 2, 1.5]
for idx in range(len(circle.history)):
    assert(circle.history[idx] == gt[idx])

assert(repr(circle) == 'Circle(radius=1.5)')
assert(str(circle) == 'Circle with radius of 1.5')

circle2 = Circle(radius=2) 
assert(circle2.history[0] == 2)

circle2.radius = 2

gt = [2, 2]
for idx in range(len(circle2.history)):
    assert(circle2.history[idx] == gt[idx])

#Circle.history

#circle2 = Circle(-2)
#Traceback (most recent call last):
#[... traceback information] ValueError: Radius cannot be negative!

circle = Circle(radius=2) 
assert(repr(circle) == 'Circle(radius=2)')

assert(circle.history[0] == 2)

#circle.radius = -1
#[... traceback information]
#raise ValueError("Radius cannot be negative!")
#ValueError: Radius cannot be negative! >>> circle

Circle(radius=2)
assert(circle.history[0] == 2)

circle = Circle()
assert(repr(circle) == 'Circle(radius=1)')
assert(circle.history[0] == 1)

#circle.diameter = -2
#Traceback (most recent call last):
#[... traceback information] ValueError: Radius cannot be negative! >>> circle
Circle(radius=1)
assert(circle.history[0] == 1)


###################

account1 = BankAccount(100.5)
account2 = BankAccount()
assert(repr(account1) == 'BankAccount(balance=100.50)')
assert(str(account1) == 'Account with balance of $100.50')
assert(repr(account2) == 'BankAccount(balance=0.00)')
assert(bool(account1) == True)
assert(bool(account2) == False) #account2.__bool__()

if account1:
    print("account1 has a positive balance.") 
else:
    print("account1 has no money!")
#account1 has a positive balance.

account1.withdraw(200)
assert(bool(account1) == False)


account1 = BankAccount(100.50) 
account2 = BankAccount()
account3 = BankAccount(100.50)

assert(not(account1 == account2))
assert(account1 == account3)
assert(not(account1 != account3))
assert(account1 != account2)
assert(not(account1 < account2))
assert(account1 > account2)
assert(not(account1 <= account2))
assert(account1 >= account2)
assert(account1 <= account3)
assert(account1 >= account3)

