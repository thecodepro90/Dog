from data.dogdata import *
from path.typefood.dinner import *
from path.typefood.lunch import *
from path.typefood.breakfast import *
def eat_path():
    print("What would you want to eat?")
    print("1 - Dinner")
    print("2 - Lunch")
    print("3 - Breakfast")
    choice5 = input("Enter: ")
    if choice5 =="1":
        dinner()
    elif choice5 =="2":
        lunch()
