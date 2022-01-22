import random

def walk_path():
    print("Ok so now on your walk you approch a dog he barks at you, what do you do?")
    print("1 - bark at dog back")
    print("2 - ignore dog")
    print("3 - FIGHT DOG")
    choice2 = input("Enter: ")
    if choice2 == "1":
        bark()
    elif choice2 =="2":
        print("You ran back home and the dog didnt chase you")
        ranback = True

    elif choice2 =="3":
        ranvar = random.randint(0,2)

        if ranvar == 1:
            for i in range(4):
                print("BARK")
                print("SCRATCH")
            print("You won, and killed the dog! and then ran back home")
            ranback = True

        elif ranvar == 2:
            for i in range(4):
                print("BARK")
                print("SCRATCH")
            print("the other dog won and you died")
            ranback = False

def bark():
    for i in range(7):
        print("BARK")
    print()
    print("The dog got mad and wants to fight! what do you do?")
    print("1 - fight")
    print("2 - run away")
    choice3 = input("Enter: ")
    if choice3 =="1":
        ranback = False
        for i in range(4):
            print("BARK")
            print("SCRATCH")
        ranback = False
        print("the dog won in the fight and you died")
        ranback = False
    elif choice3 =='2':
        print("You ran back home and the dog didnt chase you")
        ranback = True
