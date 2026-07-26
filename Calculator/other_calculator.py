import time
menu_option_other=["square","cube","power","percentage","factorial","bmi_calculator","multiplication_table","to quit"]

def other_calculation():
    def square():
        try:
            a = int(input("Enter the number: "))
        except ValueError:
            print("Enter numeric value only.")
            return
        print(f"Result is {a**2}")

    def cube():
        try:
            a=int(input("Enter number:"))
        except ValueError:
            print("Enter numeric value only.")
            return
        print(f"Result is {a**3}")

    def percentage():
        try:
            total=int(input("Enter total value from which you want to get percentage:"))
            a=int(input("Enter number:"))
        except ValueError:
            print("Enter numeric value only.")
        
        if total==0:
            print("Total can't be zero.")
            return
        
        print(f"Result is {(a/total)*100:02}%")

    def power():
        try:
            base = int(input("Enter the base number: "))
            exponent = int(input("Enter the exponent: "))
        except ValueError:
            print("Enter numeric value only.")
            return
        print(f"Result is {base ** exponent}")

    def factorial():
        try:
            num=int(input("Enter a number to get its factorial:"))
        except ValueError:
            print("Enter numeric value only.")
            return

        if num < 0:
            print("Factorial is not defined for negative numbers.\n")
            return

        fact=1
        for i in range(1,num+1):
            fact*=i
        print(f"Result is {fact}\n")

    def bmi_calculator():
        try:
            height=float(input("Enter your height in metre:"))
            weight=float(input("Enter your weight in kg:"))
        except ValueError:
            print("Enter numeric value only.")
            return

        bmi=weight/(height**2)
        report=""

        if bmi<18.5:
            report="under weight"
        elif bmi<24.9:
            report="normal weight"
        elif bmi<29.9:
            report="over weight"
        else:
            report="obese"

        print(f"Your weight:{weight:.2f} kg |Your height:{height:.2f} m |Your BMI calculation:{report.title()}\n")
    
    def multiplication_table():
        try:
            a=int(input("\nEnter a number to get it's multiplication table:"))
        except ValueError:
            print("Enter numeric value only.")
            return
        
        print(f"Multiplication table of number {a} :\n")
        for i in range(1,11):
            print(f"{a}x{i}={a*i}")
        print()
    
    other_operator=[square,cube,power,percentage,factorial,bmi_calculator,multiplication_table]

    def show_menu():
        
        print("\n"+"-"*27)
        print(f"|{'OTHER CALCULATOR MENU':^25}|")
        print("-"*27+"\n")
        print("-"*27)
        for i ,operation in enumerate(menu_option_other,start=1): 
            print(f"| {i}) {operation.title():<21}|")
        print("-"*27)

    while True:
        time.sleep(0.5)
        show_menu()

        try:
            user_choice=int(input("\nEnter your choice:"))
        except ValueError:
            print("Enter numeric value only.")
            continue

        if 1<=user_choice<=7:
            other_operator[user_choice-1]()
            
        elif user_choice==8:
            print("Exiting the program other calculation.")
            return
        
        else:
            print("Enter a valid options.")
