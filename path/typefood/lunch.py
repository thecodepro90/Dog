from data.dogdata import *
def lunch():
    typefood = "lunch"
    print(f"Ok where do you want to go for {typefood}")
    print("1 - lunch fast food")
    print("2 - eat from home(Custom food)")
    print("3 - lunch fancy food")
    choice10 = input("Enter: ")
    if choice10 =="1":
        lfastfood()
    elif choice10 =="2":
        print("At home you now get to choose what to eat so what would you like?")
        choice12 = input("Enter: ")
        d.lunch = choice12
        for i in range(4):
            print("Munch")
        print(f"mmm {d.lunch} was good!")
    elif choice12 =="3":
        lfancyfood()

    def lfastfood():
        print("What do you want from the Lunch fast food place?")
        print("1 - Burger")
        print("2 - double bacon burger")
        print("3 - dino chicken nuggets")
        choice11 = input("Enter: ")
        if choice11 =="1":
            for i in range(4):
                print("Munch")
            print("MMM that burger was SO GOOD lets go back home")
        elif choice11 =="2":
            for i in range(4):
                print("Munch")
            print("MMM that DOUBLE bacon burger was SO GOOD lets go back home")
        elif choice11 =="3":
            for i in range(4):
                print("Munch")
            print("MMM those DINO chichen NUGGETS were SO GOOD lets go back home")

    def lfancyfood():
        print("What do you want from the lunch fast food place?")
        print("1 - Fauncy burgur")
        print("2 - double bacon CHEESE burber")
        print("3 - dino chicken nuggets with chik fila sauce")
