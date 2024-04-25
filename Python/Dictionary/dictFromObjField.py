#  get a dictionary from an object's fields.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
person_dict = vars(person)   # Get dictionary from the object's fields
print("Dictionary from object's fields:", person_dict)