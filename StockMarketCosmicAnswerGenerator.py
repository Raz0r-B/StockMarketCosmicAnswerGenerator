'''
    Inspired by multiple magic 8ball programs
    This was a simple project I first learnes in the popular "Automate the boring stuff with python"
    As well as lots of googling on creating graphic user interfaces with the tkinter python library
'''

import random
import tkinter as tk

#Create class that contains 
class Magic8Ball(tk.Frame):

    def __init__(self, master=None):

        tk.Frame.__init__(self,master)
        self.grid()
        self.master.title('Exploding 8 Ball of Ape-Kittens') # titles of program/window
        self.master.configure(bg = 'white') 
        self.master.geometry("600x400")   
        self.master.resizable(0,0)        # locks window size
        self.instructionHeading()
        self.questionBox()
        self.askButton()

#Define additional parts of magic 8ball
    #Defines the heading, gives instructions
    def instructionHeading(self):
        self.heading= tk.Label(self, text='Inspired by the god of investing, Exploding Kitten. Ask a question', font=('Times New Roman', 15))
        self.heading.config(bg= 'black', fg= 'green')
        self.heading.grid(row= 1, column= 0, columnspan= 3, pady= 5, padx= 5)
    
    #Creates box for question input
    def questionBox(self):
        self.question = tk.Entry(self, width= 35)
        self.question.grid(row= 2, column= 0, columnspan= 3, pady= 5, padx= 10)
        self.question.focus_force()
        return self.question #we want to return the question asked
    
    #Creates the button to activate answer 
    def askButton(self):
        self.button = tk.Button(self, text='Ask the Ape Gods', font=('Times New Roman', 15))
        self.button.configure(bg='black',fg='white')
        self.button.grid(row= 3,column= 1, pady= 5, padx= 5)
        self.button["command"] = self.validate #waits for user to click button
        self.master.bind("<Return>", self.validate2) # runs on enter key press

    #Builds answer display
    def display(self, message): 
        answers = tk.Text(self, width= 17, height= 6, bg= 'black', fg= 'yellow', wrap= 'word')
        answers.config(font='bold')
        answers.grid(row= 4, column= 1, columnspan= 1)

    
    #inputs answer into answer box
        answers["state"] = "normal"
        answers.delete(0.0,'end')
        answers.insert(0.0,message)
        answers["state"] = "disabled"
        self.question.delete(0,'end') #This line deletes the question

    #Create validation to make sure question makes sense
    def validate(self):
        question= self.question.get()
        if question == '':
            message = "You asked nothing. I will keep my secrets"
            self.display(message)
        elif question.isdigit():
            message = "This is wrong. I am not a mathematician!"
            self.display(message)
        elif not question.endswith("?"):
            message = "Are you telling me or asking? ?<===="
            self.display(message)
        elif not " " in question:
            message = "Give me more than one word to work with"
            self.display(message)
        else:
            self.submit_answer()

    #Runs validation for keyboard press
    def validate2(self, event):
        question= self.question.get()
        if question == '':
            message = "You asked nothing. I will keep my secrets"
            self.display(message)
        elif question.isdigit():
            message = "This is wrong. I am not a mathematician!"
            self.display(message)
        elif not question.endswith("?"):
            message = "Are you telling me or asking? ?<===="
            self.display(message)
        elif not " " in question:
            message = "Give me more than one word to work with"
            self.display(message)
        else:
            self.submit_answer()  

    def submit_answer(self):
        #Set up list of responses
        response = ['Buy more GME',
                    'Buy more AMC',
                    'Sell Everything', 
                    'Go all In!',
                    'Buy Calls', 
                    'What would Buffet do?',
                    'You are a bad trader',
                    'Concentrate and ask again',
                    'My reply is no','Outlook not so good',
                    'Very doubtful', 
                    'Yes',
                    'It is certain',
                    'It is decidedly so',
                    'Dont ask this ever again',
                    'The TA has aligned!',
                    'Maybe you should ask WSB',
                    "It would be better to ask your wife's boyfriend",
                    ]

        message = random.choice(response)

        self.display(message)

        

win = Magic8Ball()
win.mainloop()

