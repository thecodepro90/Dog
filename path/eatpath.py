from data.dogdata import *

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

def dinner():
    typefood = "dinner"
    print(f"Ok where do you want to go for {typefood1}")
    print("1 - fast food")
    print("2 - eat from home(Custom food)")
    print("3 - fancy food")
    choice6 = input("Enter: ")
    if choice6 =="1":
        fastfood()
    elif choice6 =="2":
        print("At home you now get to choose what to eat so what would you like?")
        choice8 = input("Enter: ")
        d.dinner = choice8
        for i in range(4):
            print("Munch")
        print(f"mmm {d.dinner} was good!")
    elif choice6 =="3":
        fancyfood()


    def fastfood():
        print("What do you want to get from the dinner fast food place?")
        print("1 - Burger")
        print("2 - Hot dog")
        print("3 - Chicken Nuggets")
        choice7 = input("Enter: ")
        if choice7 =="1":
            for i in range(4):
                print("Munch")
            print("mmm that burger was good lets go back home!")
        elif choice7 =="2":
            for i in range(4):
                print("Munch")
            print("mmm that Hot Dog was good lets go back home!")
        elif choice7 =="3":
            for i in range(4):
                print("Munch")
            print("mmm those chicken nuggets were good lets go back home!")

    def fancyfood():
        print("What do you want to get from the dinnerfancy food place?")
        print("1 - steak")
        print("2 - salad")
        print("3 - fancy burger")
        choice9 = input("Enter: ")
        if choice9 =="1":
            for i in range(4):
                print("Munch")
            print("That steak was so exquisite now lets go back home!")
        elif choice9 =="2":
            for i in range(4):
                print("Munch")
            print("That salad was so exquisite now lets go back home!")
        elif choice9 =="3":
            for i in range(4):
                print("Munch")
            print("That fancy burger was so exquisite now lets go back home!")


def lunch():
    typefood = "lunch"
    print(f"Ok where do you want to go for {typefood1}")
    print("1 - lunch fast food")
    print("2 - eat from home(Custom food)")
    print("3 - lunch fancy food")
    choice10 = input("Enter: ")
    if choice10 =="1":
        lfastfood()

    def lfastfood():
        print("What do you want from the Lunch fast food place?")
        print("1 - Burger")
        print("2 - ")
