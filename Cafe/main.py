from Cafe_menu import Order_Menu
from order import Order
import time
ordering=True

menu=Order_Menu()
order=Order()

def options():
    options=["to order","to remove item","to get bill"]
    print("\n"+"-"*19)
    print(f"|{'OPTIONS':^17}|")
    print("-"*19)
    for i,option in enumerate(options,start=1):
        print(f"|{i}.{option.title():<15}|")
    print("-"*19)


while ordering:
    time.sleep(0.5)
    options()

    while True:
        try:
            user_choice=int(input("\nEnter your choice:"))
            if user_choice in [1,2,3]:
                break
            else:
                print("Enter valid option only.")
        except ValueError:
            print("Enter numeric value only.")

    if user_choice==1:
        order.give_order()

    elif user_choice==2:
        if order.cart:
            order.remove_item()
        else:
            print("No item in cart")

    elif user_choice==3:
        if order.cart:
            order.to_order()
            ordering=False
        else:
            print("No item in cart")

    
    
