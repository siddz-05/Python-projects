import json

APP_FUNCTIONS=["add contact","view contacts","search contact","delete contact","to quit app"]

class Contacts:
    def __init__(self):
        self.Contact_data=self.load_data()
    
    def display_menu(self):
        print("\n" + "-"*24)
        print(f"|{'CONTACT APP MENU':^22}|")
        print("-"*24)
        for i, function in enumerate(APP_FUNCTIONS, start=1):
            print(f"| {i}. {function.title():<18}|")
        print("-"*24)

    def add_contact(self):
        
        name=input("\nEnter contact name:").lower()
        while True:
            number=input("Enter contact number:")
            if number.isdigit() and len(number)==10:
                break
            else:
                print("Enter a valid contact number.\n")
        self.Contact_data[name]=number
        self.update_data()
    
    def update_data(self):
        with open("Contacts/contacts_data.json","w") as data:
            json.dump(self.Contact_data,data,indent=4)
    
    def load_data(self):
        try:
            with open("Contacts/contacts_data.json","r") as data:
                contacts=json.load(data)
        except FileNotFoundError:
            return{}
        else:
            return contacts
        
    def view_contact(self):

        if self.Contact_data:
            print("\nContact List:")
            for key,val in self.Contact_data.items():
                print(f"{key.title()}:{val}")
        else:
            print("No contacts in database.")

    def remove_contact(self):

        if self.Contact_data:
            name=input("\nEnter name to delete from contacts:").lower()
            if name in self.Contact_data:
                print(f"Contact {name.title()} is successfully removed from contacts")
                self.Contact_data.pop(name)
                self.update_data()
            else:
                print(f"No contact found with name {name.title()}")
        else:
            print("No contacts in database.")
    
    def search_contact(self):

        if self.Contact_data:
            name=input("\nEnter name to search in contacts:").lower()

            if name in self.Contact_data:
                contact_number=self.Contact_data[name]
                print("Contact found.......\n")
                print(f"Contact Name:{name.title()}")
                print(f"Contact Number:{contact_number}")
            else:
                print(f"No contact found with name {name.title()}")
        else:
            print("No contacts in database.")
