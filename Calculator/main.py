import basic_calculator
import other_calculator
import time

menu_option_basic=["addition","subtraction","multiplication","divide","remainder"]
menu_option_other=["square","cube","power","percentage","factorial","bmi calculator","multiplication table"]

def menu():
    print("\n"+"-"*22)
    print("|1. Basic calculator |")
    print("-"*22)
    for i ,operation in enumerate(menu_option_basic,start=1):
        print(f"|{i}){operation.title():<18}|")
    print("-"*22)
    time.sleep(0.2)
    print("\n"+"-"*27)
    print(f"|2.{'Other calculator':^23}|")
    print("-"*27)
    for i ,operation in enumerate(menu_option_other,start=1):
        print(f"|{i}){operation.title():<23}|")
    print("-"*27)
    time.sleep(0.2)
    print("-"*13)
    print("|3. To QUIT |")
    print("-"*13)

print("\n"+"-"*27)
print(" Welcome To Calculator App")
print("-"*27)

while True:
    time.sleep(0.5)
    menu()
    try:
        user_choice=int(input("\nEnter your choice:"))
    except ValueError:
        print("Enter numeric value only.")
        continue

    if user_choice==1:
        basic_calculator.basic_calculation()
    elif user_choice==2:
        other_calculator.other_calculation()
    elif user_choice==3:
        print("Thanks for using calculator.\n")
        break
    else:
        print("Enter valid menu option only.")