
#handles dog data
class Dog_data:
    def __init__(self, name, age, color, dinner, lunch, breakfast):
        self.name = name
        self.age = age
        self.color = color
        self.dinner = dinner
        self.lunch = lunch
        self.breakfast = breakfast
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def get_dinner(self):
        return self.dinner

    def get_lunch(self):
        return self.lunch

    def get_breakfast(self):
        return self.breakfast

d = Dog_data("name", 1, "color", "food", "food", "food")
#start virtual dog
def dogstart():
    print("hi im the Virtual_dog what would you like my name to be?")
    var = input("Enter: ")
    d.name = var
    print(f"{d.name}, thats a nice name!")
    print("What would you like my age to be?(in years)")
    var1 = input("Enter: ")
    d.age = int(var1)

    if d.age >= 10:
        old = True
    elif d.age < 10:
        old = False

    if old == True:
        print(f"dang {d.age} is old!")
    elif old == False:
        print(f"yay {d.age} is young!")

    print("Now that we're getting somewhere what would you like the color of my fur to be?")
    var2 = input("Enter: ")
    d.color = var2
    print(f"{d.color}, is a nice color!")
    print("ok a few more things, what would you like me to eat for dinner?")
    var3 = input("Enter: ")
    d.dinner = var3
    print("What do you want be to eat for lunch?")
    var4 = input("Enter: ")
    d.lunch = var4
    print("What do you want me to eat for breakfast?")
    var5 = input("Enter: ")
    d.breakfast = var5
    print(f"so for dinner ill have {d.dinner} and for lunch ill have {d.lunch} and for breakfast ill have {d.breakfast} ")

    print("So what would you like to do now?")
    print("1 - Go for a walk")
    print("2 - Eat Food")
    print("3 - Do nothing")
    var6 = input("Enter: ")

    if var6 == 1:
        path1 = True
