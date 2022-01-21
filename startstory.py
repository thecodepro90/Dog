from path.walkpath import *
from path.eatpath import *

def start_story():
    print("Ok now what do you want to do?")
    print("1 - go for a walk")
    print("2 - eat")
    print("3 - do nothing")
    choice1 = input("Enter: ")

    if choice1 == 1:
        walk_path()
    elif choice1 == 2:
        eat_path()
    else:
        pass
