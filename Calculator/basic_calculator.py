menu_option_basic=["addition","subtraction","multiplication","divide","remainder"]
def basic_calculation():
    def addition(a,b):
        return a + b
    
    def subtraction(a,b):
        return a - b

    def multiplication(a,b):
        return a * b

    def divide(a,b):
        if b == 0:
            print("Cannot divide by 0")
            return None
        return a / b    
        
    def remainder(a,b):
        if b == 0:
            print("Cannot divide by 0")
            return None
        return a%b
    
    def show_menu():
        
        print("\n"+"-"*27)
        print(f"|{'BASIC CALCULATOR MENU':^25}|")
        print("-"*27+"\n")
        print("-"*21)
        for i ,operation in enumerate(menu_option_basic,start=1): 
            print(f"| {i}) {operation.title():<15}|")
        print("-"*21)
    
    symbol={"addition":"+","subtraction":"-","multiplication":"*","divide":"/","remainder":"%"}
    available_calculation=[addition,subtraction,multiplication,divide,remainder]
    result=0
    with_result=False

    while True:

        if not with_result:
            while True:
                try:
                    a=float(input("\nEnter the first number:"))
                    break
                except ValueError:
                    print("Enter numeric value only.")
        else:
            a=result
        
        show_menu()
        
        while True:  
            try:
                user_choice=int(input("\nEnter your choice:"))
                if 1<=user_choice <= len(menu_option_basic):
                    break
                else:
                    print("Enter a valid option number.")
            except ValueError:
                print("Enter numeric value only.")
        
        while True:
            try:
                b=float(input("\nEnter second number:"))
                break
            except ValueError:
                print("Enter numeric value only.")

        result=available_calculation[user_choice-1](a,b)
        
        if result is None:
            with_result = False
            continue

        print(f"{a} {symbol[menu_option_basic[user_choice - 1]]} {b} = {result}")

        while True:
            next_calculation= input("\nContinue with result (y), new calculation (n), or quit (q)? ").lower()
            if next_calculation in ['y','n','q']:
               break
            else:
                print("Enter a valid option.")
                
        if next_calculation=='y':
            with_result=True
        elif next_calculation=='n':
            with_result=False
        else:
            print("Exiting the basic calculator.")
            return