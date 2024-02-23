from cProfile import label
import email
from importlib.metadata import entry_points
from logging import getLogger
import string
import tkinter as tk
from tkinter import ttk
from typing import Container
import customtkinter
from openpyxl import*



LARGEFONT = ("Verdana", 35)

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = customtkinter.CTkFrame(self)
        container.grid (side="top", fill = "both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)

        app = customtkinter.CTk()
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)

        self.frames = {}

        for F in (RegistrationPage, LoginPage, WelcomePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(RegistrationPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class RegistrationPage(customtkinter.CTkFrame):
    global name_field
    global passentry1
    global passentry2
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
       


        def display_text():
            global p1string
            global p2string
            global strin
            strin=name_field.get()
            p1string= passentry1.get()
            p2string=passentry2.get()
            if (p1string != p2string
            ):
                label.configure(text="Passwords Don't match ")

            else:
                controller.show_frame(LoginPage)

        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.grid(row=0, column=3, sticky="nsew")
        frame_1.grid_rowconfigure(10, weight=1)
        frame_1.grid_rowconfigure(2, minsize=30)

        label_1 = customtkinter.CTkLabel(master=frame_1, text="Welcome", text_font=("Roboto Medium", 20))
        label_1.grid(row=0, column = 0, columnspan=1, padx=5, pady=5, sticky="ew")

        name_field=customtkinter.CTkEntry(master=frame_1,
                                            width=320,
                                            placeholder_text="Username")
        name_field.grid(row=3, column=0, pady=5, padx= 25, sticky="n")

        passentry1=customtkinter.CTkEntry(master=frame_1,
                                            width=320,
                                            placeholder_text="Type Password")
        passentry1.grid(row=4, column=0, pady=5, padx=25, sticky="n")

        passentry2=customtkinter.CTkEntry(master=frame_1,
                                            width=320,
                                            placeholder_text="Retype Password")
        passentry2.grid(row=5, column= 0, pady=5, padx= 25, sticky="n")

        submit=customtkinter.CTkButton(master=frame_1, text= "Register", fg_color=("gray75", "gray30"), command=display_text)
        submit.grid(row=6, column=0, pady=10, padx=20)

        label= customtkinter.CTkLabel(master=frame_1, text="", font=("courier 22 bold"))
        label.pack()
        display_text()
class LoginPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent)

        

        def welcome(p2string):
            username= usern.get()
            passwo=passw.get()
            if (passwo != p2string or username != strin 
            ):
                label.configure(text=" invalid username or password")
            else:
                controller.show_frame(WelcomePage)

        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.grid(row=0, column=3, sticky="nsew")
        frame_1.grid_rowconfigure(10, weight=1)
        frame_1.grid_rowconfigure(2, minsize=30)


        label1 = customtkinter.CTkLabel(maste=frame_1, text="Login", text_font=("Roboto Medium 22 bold"))
        label1.grid(row=0, column=0, pady=5 , padx=5, sticky="ew" )

        usern=customtkinter.CTkEntry(master=frame_1,
                                         placeholder_text="Username",
                                         width=320)
        usern.grid(row=3, column=0, pady=5, padx=25, sticky="n")

        passw=customtkinter.CTkEntry(master= frame_1,
                                    placeholder_text="Password",
                                    width=320)
        passw.grid(row=4, column=0, pady=5, padx=25, sticky="n")

        submit=customtkinter.CTkButton(master=frame_1, text="Submit", fg_color=("gray75", "gray30"), command=welcome)
        submit.grid(row=5, column=1, pady=10, padx=20)

        label= customtkinter.CTkLabel(master=frame_1, text="", font=("courier 22 bold"))
        label.pack()

class WelcomePage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):

        customtkinter.CTkFrame(parent, controller)

        frame_1 = customtkinter.CTkFrame(master=self)
        frame_1.grid(row=0, column=3, sticky="nsew")
        frame_1.grid_rowconfigure(10, weight=1)
        frame_1.grid_rowconfigure(2, minsize=30)

        welcomeLabel=customtkinter.CTkLabel(master=frame_1, text="Welcome" + strin)
        welcomeLabel.grid(row=2, column=0)

app = tkinterApp()
app.mainloop()