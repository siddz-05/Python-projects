from tkinter import *
from random import randint,choice,shuffle
import pyperclip
import json
from tkinter import messagebox

BACKGROUND="#918DCE"
EMAIL="xyz123@gmail.com"

def load_data():
    try:
        with open("password_manager/password_data.json","r") as file:
            password_data=json.load(file)
        return password_data
    except FileNotFoundError:
        return{}

def password_generate():
    password_entry.delete(0,END)
    character="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol="!@#$%^&*()"
    number="1234567890"

    letter=[choice(character) for _ in range(randint(6,8))]
    num=[choice(number) for _ in range(randint(4,6))]
    sym=[choice(symbol) for _ in range(randint(2,4))]

    password=letter+num+sym
    shuffle(password)
    Password="".join(password)
    password_entry.insert(END,Password)
    pyperclip.copy(Password)

def save_password():
    username=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    data=load_data()
    data[username]={"Email":email,"Password":password}

    if username!="" and password!="":
        done=messagebox.askyesno(title=username,message=f"Email:{email}\nPassword:{password}")
        if done:
            with open("password_manager/password_data.json","w") as file:
                json.dump(data,file,indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error",message="Field entry can't left empty")

def search_password():
    website=website_entry.get()

    data=load_data()

    if website!="":
        if website in data:
            website_data=data[website]
            messagebox.showinfo(title=website,message=f"Email:{website_data['Email']}\nPassword:{website_data['Password']}")
        else:
            messagebox.showinfo(title="Data not found",message=f"No detail found of {website}.")
    else:
        messagebox.showerror(title="Error",message="Field entry can't left empty")
        
#UI
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg=BACKGROUND)
canvas=Canvas(width=318,height=180,highlightthickness=0,bg=BACKGROUND)
pass_image=PhotoImage(file="password_manager/background.png")
canvas.create_image(159,80,image=pass_image)
canvas.grid(row=0,column=1)


#Labels
website_label=Label(text="Website:",bg=BACKGROUND,font=("Arial", 10,"bold"))
website_label.grid(row=1,column=0)
email_label=Label(text="Email:",bg=BACKGROUND,font=("Arial", 10,"bold"))
email_label.grid(row=2,column=0)
password_label=Label(text="Password:",bg=BACKGROUND,font=("Arial", 10,"bold"))
password_label.grid(row=3,column=0)

#Enteries
website_entry=Entry(width=51)
website_entry.focus()
website_entry.grid(row=1,column=1)
email_entry=Entry(width=51)
email_entry.insert(END,EMAIL)
email_entry.grid(row=2,column=1)
password_entry=Entry(width=51)
password_entry.grid(row=3,column=1)

#Button
password_button=Button(text="Generate Password",command=password_generate)
password_button.grid(row=3,column=2)
search_button=Button(text="Search",width=15,command=search_password)
search_button.grid(row=1,column=2)
add_button=Button(text="Add",width=43,command=save_password)
add_button.grid(row=4,column=1)


window.mainloop()