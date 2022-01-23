from startstory import *
from data.dogdata import *


d = Dog_data("name", 1, "color", "food", "food", "food")


def tryagain():
    print("Do you want to try again?")
    print("1 - yes")
    print("2 - no")
    choice4 = input("Enter: ")
    if choice4 =="1":
        start()
    elif choice4 == "2":
        pass

def start():
    print("Started!")
    startdog()
    start_story()

start()
