from collections import namedtuple

# Define a named tuple type called 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create instances of the named tuple
p1 = Point(1, 2)
p2 = Point(3, 4)

# Access fields using the named attributes
print("p1:", p1.x, p1.y)  # Output: p1: 1 2
print("p2:", p2.x, p2.y)  # Output: p2: 3 4
