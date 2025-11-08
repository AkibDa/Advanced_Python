class Person:
  
  def __init__(self, name, age, gender):
    self.__name = name
    self.__age = age
    self.__gender = gender
  
  @property  
  def Name(self):
    return self.__name
  
  @Name.setter
  def Name(self, name):
    if not name:
      raise ValueError("Name cannot be empty")
    self.__name = name
    
  @staticmethod
  def is_adult(age):
    return age >= 18
    
p1 = Person("Miles", 18, 'm')
print(p1.Name)