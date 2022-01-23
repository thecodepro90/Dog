class Dog_data:
    def __init__(self, name, age, color, dinner, lunch, breakfast):
        self.name = name
        self.age = age
        self.color = color
        self.dinner = dinner
        self.lunch = lunch
        self.breakfast = breakfast
        self.is_alive = True

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def get_dinner(self):
        return self.dinner

    def get_lunch(self):
        return self.lunch

    def get_breakfast(self):
        return self.breakfast

    def get_is_alive(self):
        return self.is_alive

    # def set_is_alive(status):
    #     self.is_alive = status
