from shapes import Point, Circle


point1 = Point(2, 3)
point2 = Point(4, 5)

id1 = id(point1)
id2 = id(point2)

point3 = point1 + point2
print(point3)

assert(id1 == id(point1))
assert(id2 == id(point2))

point1 += point2
print(point1)

assert(id1 == id(point1)) # Should be unchanged True
print(point2) # Should be unchanged

point1 = Point(2, 3)
point3 = point1 * 3
print(point3)

point2 = Point(4, 5)
point4 = 2 * point2
print(point4)

id1 = id(point1)
point1 *= 4
print(point1)
assert(id1 == id(point1))

point = Point(2, 3)
x, y = point
print(x, y)


