from contact import Contacts
import time

contact=Contacts()

while True:
    time.sleep(1)
    contact.display_menu()

    try:
        user_choice=int(input("\nChoose a options:"))
    except ValueError:
        print("Enter numeric value only")
    
    if user_choice==1:
        contact.add_contact()
    
    elif user_choice==2:
        contact.view_contact()
    
    elif user_choice==3:
        contact.search_contact()
    
    elif user_choice==4:
        contact.remove_contact()
    
    elif user_choice==5:
        print("Thanks for using contact app.\n")
        break
    
    else:
        print("Choose valid option.")