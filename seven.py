from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
  
  @abstractstaticmethod
  def speak():
    """ Interface Method """
    pass
  
# p1 = IPerson()  // This will raise an error
# p1.speak()

class Student(IPerson):
  
  def __init__(self):
    self.name = "Basic Student Name"

  def speak(self):
    print(f"My name is {self.name}")

class Teacher(IPerson):
  
  def __init__(self):
    self.name = "Basic Teacher Name"

  def speak(self):
    print(f"My name is {self.name}")
    
s1 = Student()
s1.speak()

t1 = Teacher()
t1.speak()

class PersonFactory:
  
  @staticmethod
  def get_person(person_type: str) -> IPerson:
    if person_type == "student":
      return Student()
    elif person_type == "teacher":
      return Teacher()
    else:
      raise ValueError("Unknown person type")
    
if __name__ == "__main__":
  choice = input("Enter person type (student/teacher): ").strip().lower()
  
  person = PersonFactory.get_person(choice)
  person.speak()
  