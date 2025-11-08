class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __del__(self):
    print(f"Person {self.name} is being deleted")
    
class Vector:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  
  def __repr__(self):
    return f"X: {self.x}, Y: {self.y}"
  
  def __len__(self):
    return (self.x**2 + self.y**2)**0.5
  
  def __call__(self, *args, **kwds):
    print(f"Vector called with args: {args} and kwds: {kwds}")
    
  def __del__(self):
    print(f"Vector ({self.x}, {self.y}) is being deleted")
  
p = Person("Alice", 30)
del p

v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
print(v3)
print(f"Length of v3: {len(v3)}")
v3(10, 20, key='value')
del v1
del v2
del v3