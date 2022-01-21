from data.dogclass import *

d = Dog_data("name", 1, "color", "food", "food", "food")

def startdog():
    print("Hi im Virtual dog we're gonna do alot of fun stuff but first what do you want my name to be?")
    name = input("Enter: ")
    d.name = name
    print(f"{d.name} is a nice name!")
    print("What should my age be?")
    age = int(input("Enter: "))
    d.age = age
    if age > 10:
        print(f"Dang {d.age} is old!")
    else:
        print(f"Yay {d.age} is young!")
    print("What color should my fur be?")
    color = input("Enter: ")
    d.color = color
    print(f"{d.color} is a nice color!")
