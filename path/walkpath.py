
def walk_path():
    print("Ok so now on your walk you approch a dog he barks at you, what do you do?")
    print("1 - bark at dog back")
    print("2 - ignore dog")
    print("3 - FIGHT DOG")
    choice2 = input("Enter: ")
    if choice2 == "1":
        bark()

def bark():
    for i in range(7):
        print("BARK")
    print()
    print("The dog got mad and wants to fight! what do you do?")
    print("")
