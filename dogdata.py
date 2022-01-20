from dogclass import *

d = Dog_data("name", 1, "color", "food", "food", "food")

print("Hi im Virtual dog we're gonna do alot of fun stuff but first what do you want my name to be?")
name = input("Enter: ")
d.name = name
print(f"{d.name} is a nice name!")
