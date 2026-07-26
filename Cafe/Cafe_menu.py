
MENU=["pizza", "burger", "cold coffee", "mojhito", "pasta", "noodle", "icecream"]
PRICE=[200, 150, 100, 120, 175, 100, 100]

class Order_Menu:
    def __init__(self):
        self.cafe_menu=MENU
        self.price=PRICE
        self.title()
        self.show_menu()

    def title(self):
        print("\n"+"-"*30)
        print(" WELCOME TO SIDDHARTH'S CAFE! ")
        print("-"*30)

    def show_menu(self):
        print("\n"+"-"*25)
        print(f"|{'CAFE MENU':^23}|")
        print("-"*25)
        print(f"|{'ITEM':^13}|{'PRICE':^9}|")
        print("-"*25)
        for i,items in enumerate(self.cafe_menu): 
            print(f"|{items.title():<13}| ₹{self.price[i]}.00 |")   
        print("-"*25)
