class Dog_data:
    def __init__(self, name, age, color, msg, food):
        self.name = name
        self.age = age
        self.color = color
        self.msg = msg
        self.food = food



d = Dog_data("name", 1, "color", "msg", "food")

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
    print(f"dang {d.age} im old!")
elif old == False:
    print(f"yay {d.age} is young!")
