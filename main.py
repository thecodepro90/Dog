class Dog_data:
    def __init__(self, name, age, color, dinner, lunch, breakfast):
        self.name = name
        self.age = age
        self.color = color
        self.food = food
        self.dinner = dinner
        self.lunch = lunch
        self.breakfast = breakfast






d = Dog_data("name", 1, "color", "food", "food", "food")
print("hi im the Virtual_dog what would you like my name to be?")
var = input("Enter: ")
d.name = var
print(f"{d.name}, thats a nice name!")
print("What would you like my age to be?")
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
