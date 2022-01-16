
class Person:
    number_of_people = 0

    def __init__(self, name):
         self.name = name

p1 = Person("tim")
p2 = Person("jill")
print(p2.number_of_people)
Person.number_of_people = 8
print(p2.number_of_people)
