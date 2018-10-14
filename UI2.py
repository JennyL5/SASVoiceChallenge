import tkinter as tk
from tkinter import messagebox

LARGE_FONT = ("Verdana", 12)

#LINK DATABSE
#Voice recognition using pocketsphinx

#loop for number of columns in database

#for i in n:
    #read in qs
    #read in list of answers

    ##have a function to read everything from db
         # read in list of questions
         # read in all links
              # read in each list from each link

    # for i in n:
    #when start button is pressed call function:
    # import ith element for: question and list of possible answers
    # read in from audio recognition


def callback1():
    answer1 = "I am curious"  # voice input
    list1 = ['curious', 'passionate', 'responsible'] #from db
    str1 = answer1.split()

    # print(str1)
    messagebox.showinfo("Question1", answer1) #from db
    result = any(elem in str1 for elem in list1)
    if result:
        messagebox.showinfo("Pass", 'You have passed! Move onto next question.')
    else:
        messagebox.showinfo("Failed", 'You have failed!')


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Start, window):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The audio interview will begin once you press start.", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Start", command=lambda: controller.show_frame(window))
        button1.pack()


class window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Question 1: ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Record", command=callback1)
        button1.pack()

        button2 = tk.Button(self, text="Submit", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


def end():
    messagebox.showinfo("End", "This is the end of the interview.")


app = SeaofBTCapp()
app.mainloop()
