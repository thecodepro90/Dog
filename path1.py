from main import Dog_data

d = Dog_data("name", 1, "color", "food", "food", "food")


def path1():
    d.get_name = d.name
    d.get_age = d.age
    d.get_color = d.color
    d.get_lunch = d.lunch
    d.get_dinner = d.dinner
    d.get_breakfast = d.breakfast

    print("ok now while your on your walk you approch a dog what do you do?")
    print("1 - Bark at the dog")
    print("2 - Ignore the dog")
