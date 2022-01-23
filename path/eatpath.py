from data.dogdata import *

def eat_path():
    print("What would you want to eat?")
    print("1 - Dinner")
    print("2 - Lunch")
    print("3 - Breakfast")
    choice5 = input("Enter: ")
    if choice5 =="1":
        dinner()




def dinner():
    typefood1 = "dinner"
    print(f"Ok where do you want to go for {typefood1}")
    print("1 - fast food")
    print("2 - eat from home(Custom food)")
    print("3 - fancy food")
