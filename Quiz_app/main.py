from tkinter import *
from question_bank import QuestionBank
from tkinter import messagebox
BACKGROUND="#6690EB"

class Quiz_app:

    def __init__(self,question_data:QuestionBank):
        self.answer=None
        self.score=0
        self.questions=question_data
        self.window=Tk()
        self.window.title("QuizArena")
        # self.window.minsize(width=500,height=400)
        self.window.config(padx=50,pady=50,bg=BACKGROUND)

        self.title_label=Label(text="Trivia Universe: Explore, Learn, and Compete",font=("Arial", 15,"bold"),background=BACKGROUND)
        self.title_label.grid(row=0,column=0)


        self.question_label=Label(text="Q1.sample text?",bg=BACKGROUND, font=("Arial", 12,"bold"), wraplength=500)
        self.question_label.grid(row=2,column=0,sticky="w")

        self.radiostate=StringVar()

        self.option1=Radiobutton(text="option1",value=1,variable=self.radiostate,bg=BACKGROUND,font=("Arial", 12,"italic"))
        self.option1.grid(row=3,column=0,sticky="w")

        self.option2=Radiobutton(text="option2",value=2,variable=self.radiostate,bg=BACKGROUND,font=("Arial", 12,"italic"))
        self.option2.grid(row=4,column=0,sticky="w")

        self.option3=Radiobutton(text="option3",value=3,variable=self.radiostate,bg=BACKGROUND,font=("Arial", 12,"italic"))
        self.option3.grid(row=5,column=0,sticky="w")

        self.option4=Radiobutton(text="option4",value=4,variable=self.radiostate,bg=BACKGROUND,font=("Arial", 12,"italic"))
        self.option4.grid(row=6,column=0,sticky="w")

        button_image=PhotoImage(file="Quiz_app/button.png")
        self.next_button=Button(image=button_image,command=self.check_answer,bg=BACKGROUND,pady=30,borderwidth=0, highlightthickness=0,padx=15)
        self.next_button.grid(row=7,column=0,sticky="w")

        self.canvas=Canvas(width=275,height=183,highlightthickness=0,background=BACKGROUND)
        quiz_image=PhotoImage(file="Quiz_app/title.png")
        self.canvas.create_image(137,91,image=quiz_image)
        self.canvas.grid(row=1,column=0)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.radiostate.set(None)
        no,question,option,self.answer=self.questions.get_question()
        
        if no <=20:
            self.question_label.config(text=f"Q{no}.{question}")

            self.option1.config(text=option[0],value=option[0])
            self.option2.config(text=option[1],value=option[1])
            self.option3.config(text=option[2],value=option[2])
            self.option4.config(text=option[3],value=option[3])
        
        if no==20:
            self.next_button.config(command=self.finish_quiz)
            
    def finish_quiz(self):

        self.question_label.config(text=f"Congratulation on completing the Quiz. Your score is {self.score}/20.")
        self.option1.destroy()
        self.option2.destroy()
        self.option3.destroy()
        self.option4.destroy()

        self.next_button.destroy()

    def check_answer(self):
        user_answer=self.radiostate.get()
        
        if user_answer=="None":
            messagebox.showerror(title="Error",message="Select a option before submiting answer.")

        else:
            if user_answer==self.answer:
                self.score+=1
        
            self.next_question()

question=QuestionBank()
quiz=Quiz_app(question)