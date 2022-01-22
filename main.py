from startstory import *
from data.dogdata import *



def tryagain():
    print("Do you want to try again?")
    print("1 - yes")
    print("2 - no")
    choice4 = input("Enter: ")
    if choice4 =="1":
        start()
    elif choice4 == "2":
        break

def start():
    print("Started!")
    startdog()
    start_story()

start()
