MENU=["pizza", "burger", "cold coffee", "mojhito", "pasta", "noodle", "icecream"]
PRICE=[200, 150, 100, 120, 175, 100, 100]

class Order:
    def __init__(self):
        self.menu=MENU
        self.price=PRICE
        self.cart=[]
        self.bill=[]

    def give_order(self):
        
        while True:
            user_order=input("\nEnter the item to order:").lower()
            if user_order in self.menu:
                break
            else:
                print("Enter item to order which is in the menu.")
        
        item_index=self.menu.index(user_order)
        item_price=self.price[item_index]

        while True:
            try:
                quantity=int(input(f"\nEnter the quantity of {user_order.title()} to order:"))
                if quantity <=0:
                    print("Quantity can't be zero or negative.")
                else:
                    break
            except ValueError:
                print("Enter numeric value only.")
        
        subtotal=item_price*quantity

        print(f"{user_order.title()} is added to cart. Subtotal=₹{subtotal:.2f}")

        self.bill.append(subtotal)
        self.cart.append([user_order,quantity,item_price])

    def customer_order(self):
        print("\n"+"-"*51)
        print(f"|{'YOUR ORDER':^49}|")
        print("-"*51)
        print(f"|{'No.'}|{'Order Item':^12}|{'Quantity':^10}|{'PRICE':^10}|{'Subtotal':^10}|")
        print("-"*51)
        for i,(item,quantity,price) in enumerate(self.cart,start=1):
            subtotal=price*quantity
            print(f"|{i:02d} | {item.title():<11}| {quantity:<9}| ₹{price:<8.02f}| ₹{subtotal:<8.2f}|")
            print("-"*51)

    def remove_item(self):

        self.customer_order()

        remove=True
        while remove:
            remove_item=input("\nEnter the item to get remove from cart or 'no' to cancel remove :").lower()
            if remove_item=="no":
                return
            for item in self.cart:
                if item[0]==remove_item:
                    subtotal=item[1]*item[2]
                    print(f"{remove_item.title()} is removed from cart. Subtotal=₹{subtotal:.2f}")
                    self.bill.remove(subtotal)
                    self.cart.remove(item)
                    remove=False
            if remove:
                print("Item not in the cart.")
        
        self.customer_order()

    def to_order(self):
        self.customer_order()
        total=sum(self.bill)
        print(f"{'|':<26}|{'TOTAL BILL':^12}| ₹{total:<8.2f}|")
        print("-"*51+"\n")         
        