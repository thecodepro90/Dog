class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def get_food(self):
        return self.food

class Dog(Pet):
    def __init__(self, name, age, color, food, message):
       super().__init__(name, age, color)
       self.food = food
       self.message = message

    def speak(self):
        message = self.message
        return message

    def eat_food(self):
        print(f"Munch Munch this is some good {self.food}")

    def set_food(self,food):
        self.food = food

    def set_speak_message(self, message):
        self.message = message

d = Dog("Tim", 12, "Blue", "Steak", "Bark")
print(d.speak())
d.set_speak_message("this is different")
print(d.speak())
