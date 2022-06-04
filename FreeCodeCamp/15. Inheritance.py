# Inheritance

# Creating Classes

class chef:

    def __init__(self):

        self.appetizer = ["01. Garden Salad"]
        self.maincourse = ["01. Fried Noodles"]
        self.dessert = ["01. Jelly"]

    def must_know(self):

        print("\nAppetizer:\n" + self.appetizer[0])
        print("\nMain Course:\n" + self.maincourse[0])
        print("\nDesserts:\n" + self.dessert[0])

class western_chef(chef):

    def __init__(self):

        super().__init__()

        self.appetizer.append("02. Toasts")
        self.maincourse.append("02. Spaghetti")
        self.dessert.append("02. Ice Cream")

    def menu(self):

        print("\nAppetizer:\n" + '\n'.join(self.appetizer))
        print("\nMain Course:\n" + '\n'.join(self.maincourse))
        print("\nDesserts:\n" + '\n'.join(self.dessert))

class eastern_chef(chef):

    def __init__(self):

        super().__init__()

        self.appetizer.append("02. Steam Peanuts")
        self.maincourse.append("02. Fried Rice")
        self.dessert.append("02. Red Bean Soup")

    def menu(self):

        print("\nAppetizer:\n" + '\n'.join(self.appetizer))
        print("\nMain Course:\n" + '\n'.join(self.maincourse))
        print("\nDesserts:\n" + '\n'.join(self.dessert))

# Creating Objects

chef = chef()
GordonRamsay = western_chef()
KennyChan = eastern_chef()

print(chef.must_know())
print(GordonRamsay.menu())
print(KennyChan.menu())