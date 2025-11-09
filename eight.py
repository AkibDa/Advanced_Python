from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
  
  @abstractstaticmethod
  def speak():
    """ Interface Method """
    
class Person(IPerson):
  
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"My name is {self.name}")
    
class ProxyPerson(IPerson):
  
  def __init__(self, name):
    self._real_person = None
    self.name = name

  def speak(self):
    if self._real_person is None:
      self._real_person = Person(self.name)
    self._real_person.speak()
    
p1 = Person("Alice")
p1.speak()

p2 = ProxyPerson("Bob")
p2.speak()