#test with given inputs (window1 and window2)
#user interface runs
#not linked with db or voice recognition via sphinx

import tkinter as tk
from tkinter import messagebox

LARGE_FONT = ("Verdana", 12)


def callback1():
    answer1 = "I am curious"  # voice input
    list1 = ['curious', 'enthusiastic', 'responsible']
    str1 = answer1.split()
    # print(str1)
    messagebox.showinfo("Question1", answer1)
    result = any(elem in str1 for elem in list1)
    if result:
        messagebox.showinfo("Pass", 'You have passed! Move onto next question.')
    else:
        messagebox.showinfo("Failed", 'You have failed!')


def callback2():
    answer2 = "I really like working"  # voice input
    list2 = ['data', 'analytics', 'problem solving']
    str2 = answer2.split()
    # print(str2)
    messagebox.showinfo("Question2", answer2)
    result = any(elem in str2 for elem in list2)
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

        for F in (start, window1, window2):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Start", command=lambda: controller.show_frame(window1))
        button1.pack()


class window1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Question 1: ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Record", command=callback1)
        button1.pack()

        button2 = tk.Button(self, text="Submit", command=lambda: controller.show_frame(window2))
        button2.pack()


def end():
    messagebox.showinfo("End", "This is the end of the interview.")


class window2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Question 2: ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Record", command=callback2)
        button1.pack()

        button2 = tk.Button(self, text="Submit", command=end)
        button2.pack()


app = SeaofBTCapp()
app.mainloop()
