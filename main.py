class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_name(self):
        return name

    def get_age(self):
        return age

    def get_color(self):
        return color

class Dog(Pet):
    def __init__(self, food):
        self.food = food

    def bark(self):
        return "Bark"

    def eat_food(self):
        return "Munch Munch this is some good {self.food}"

    def set_food(self, food):
        self .food = food
