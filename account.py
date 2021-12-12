#from _typeshed import Self
import re
import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
import os
import re                                   # generally for checking if specific character is or is not included in string
from entries_validation import *

# nationalities list is in entries_validation_functions.py file



# First screen of the program. 
class CurrnetScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainLogInScreen)
        
    def switch_frame(self, frame_class):
        """Destroys current frame and replace it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def change_geometry(self, first_dim, second_dim):
        self.geometry(first_dim+"x"+second_dim)
     
class MainLogInScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.change_geometry("300", "300")
        
        tk.Label(self, text="Flight search", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        tk.Label().pack()
        tk.Button(self,text="Login", width="30", command=lambda: master.switch_frame(SignInScreen), pady=10).pack()
        tk.Label().pack()
        tk.Button(self, text="Register", width="30", command=lambda:master.switch_frame(RegistrationScreen), pady=10).pack()
    


# Window with log in form
class SignInScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Please enter your details below: ", pady=10, font=("Calibri", 15)).pack()

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        tk.Label(self, text="Username * ", font=("Calibri", 13)).pack()
        self.username_entry_log = tk.Entry(self, textvariable=self.username_verify,font=("Calibri", 13)).pack()

        tk.Label(self, text="Password * ", font=("Calibri", 13)).pack()
        self.password_entry_log = tk.Entry(self, textvariable=self.password_verify,font=("Calibri", 13)).pack()

        tk.Button(self, text="Login", command=lambda: self.login_verify(self.username_verify, self.password_verify, self.username_entry_log, self.password_entry_log) ,pady=5,padx=15,font=("Calibri", 12)).pack()

    # Verification of given username and password
    def login_verify(self, username_to_verify, password_to_verify, username_entry, password_entry):
        username = username_to_verify.get()
        password = password_to_verify.get()

        #username_entry.delete(0,'end')
        #password_entry.delete(0,'end')
        
        # Happens when the sign-in procedure is complete --- username and password are correct 
        def login_success():
            
            #try:
                #registration_window.destroy()
            #except:
                #print("")
            print("SUCCES!")

        def user_not_found():
            messagebox.showerror("Wrong username","User not found, try another username.")
        
        
        def password_not_recognised():
            messagebox.showerror("Wrong password","Wrong password, try again.")


        self.list_of_files = os.listdir("Users/")
        if username in self.list_of_files:
            self.file1 = open("Users/"+username, "r")
            self.verify = self.file1.read().splitlines()
            if password == self.verify[1]:
                print("login success")
                login_success()
            else:
                print("password has not been recognized")
                password_not_recognised()
        else:
            print("User not found")
            user_not_found()
            



def register_user(register_data, entries, error_labels):
    validation_table = [0,0,0,0,0,0,0,0,0]
    infos = []
    # register_data is a list of StringVar - special TKinter variable, that can not be simple read
    # So we need to create a list of Strings based on values of those StringVars
    for item in register_data:                      
        infos.append(item.get())


    validation_table = check_entries(infos, entries, error_labels, validation_table)
    
    if all(validation_table):
        file = open("Users/"+infos[0],"w")
        
        # "len(infos)-1" because gender is the last one. 
        # It's being written to the file separately, few lines below
        # There was a problem when it was put in the loop, because 
        # gender is radiobutton, not an entry
        # Whole problem probably can be solved by an exception
        for number in range(0,len(infos)-1):        
            file.write(infos[number]+"\n")
            entries[number].delete(0,tk.END)
        file.write(infos[len(infos)-1])
        file.close
        #registration_window.destroy()




# Binding functions
def username_color_white(event):
    username_entry.configure(bg="#ffffff")
def password_color_white(event):
    password_entry.configure(bg="#ffffff")
def password_confirmation_color_white(event):
    password_confirmation_entry.configure(bg="#ffffff")
def name_color_white(event):
    name_entry.configure(bg="#ffffff")
def surname_color_white(event):
    surname_entry.configure(bg="#ffffff")
def email_color_white(event):
    email_entry.configure(bg="#ffffff")
def age_color_white(event):
    age_entry.configure(bg="#ffffff")
def phone_number_color_white(event):
    phone_number_entry.configure(bg="#ffffff")


# Window with registration form
class RegistrationScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.change_geometry("300", "950")    # geometry ("300x850")
    

        #global username, password, username_entry, password_entry, password_confirmation, password_confirmation_entry, email, email_entry, age, age_entry, name, name_entry, surname, surname_entry,nationality, nationality_entry, gender, phone_number, phone_number_entry            # Add remained to the registration form!!!
        global username_entry, password_entry, password_confirmation_entry, email_entry, age_entry,  name_entry, surname_entry, nationality_entry, phone_number_entry
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password_confirmation = tk.StringVar()
        self.name = tk.StringVar()
        self.surname = tk.StringVar()
        self.email = tk.StringVar()
        self.nationality = tk.StringVar()
        self.gender = tk.StringVar()
        self.gender.set("Female")
        self.phone_number = tk.StringVar()
        self.age = tk.StringVar()


        tk.Label(self, text="Please enter your details below: ", pady=10, font=("Calibri", 15)).grid(row=0, column=0,columnspan=2)

        # Username entry
        self.label = tk.Label(self, text="Username * ", font=("Calibri", 13)).grid(row=1,column=0,columnspan=2)
        username_entry = tk.Entry(self, textvariable=self.username, font=("Calibri", 13),)
        username_entry.grid(row=2,column=0,columnspan=2)
        self.username_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.username_error_label.grid(row=3,column=0,columnspan=2)

        # Password entry
        tk.Label(self, text="Password * ",font=("Calibri", 13)).grid(row=4,column=0,columnspan=2)
        password_entry = tk.Entry(self, textvariable=self.password, font=("Calibri", 13), show="*")
        password_entry.grid(row=5,column=0,columnspan=2)
        self.password_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.password_error_label.grid(row=6,column=0,columnspan=2)

        # Password confirmation entry
        tk.Label(self, text="Confirm password * ",font=("Calibri", 13)).grid(row=7,column=0,columnspan=2)
        password_confirmation_entry = tk.Entry(self, textvariable=self.password_confirmation, font=("Calibri", 13), show="*")
        password_confirmation_entry.grid(row=8,column=0,columnspan=2)
        self.password_confirmation_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.password_confirmation_error_label.grid(row=9,column=0,columnspan=2)

        # Name entry
        tk.Label(self, text="Name * ",font=("Calibri", 13)).grid(row=10,column=0,columnspan=2)
        name_entry = tk.Entry(self, textvariable=self.name, font=("Calibri", 13))
        name_entry.grid(row=11,column=0,columnspan=2)
        self.name_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.name_error_label.grid(row=12,column=0,columnspan=2)

        # Surname entry
        tk.Label(self, text="Surname * ",font=("Calibri", 13)).grid(row=13,column=0,columnspan=2)
        surname_entry = tk.Entry(self, textvariable=self.surname, font=("Calibri", 13))
        surname_entry.grid(row=14,column=0,columnspan=2)
        self.surname_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.surname_error_label.grid(row=15,column=0,columnspan=2)

        # Email entry
        tk.Label(self, text="Email * ",font=("Calibri", 13)).grid(row=16,column=0,columnspan=2)
        email_entry = tk.Entry(self, textvariable=self.email, font=("Calibri", 13))
        email_entry.grid(row=17,column=0,columnspan=2)
        self.email_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.email_error_label.grid(row=18,column=0,columnspan=2)

        # Age entry
        tk.Label(self, text="Age * ",font=("Calibri", 13)).grid(row=19,column=0,columnspan=2)
        age_entry = tk.Entry(self, textvariable=self.age, font=("Calibri", 13))
        age_entry.grid(row=20,column=0,columnspan=2)
        age_entry.delete(0,tk.END)
        self.age_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.age_error_label.grid(row=21,column=0,columnspan=2)
        
        # Nationality - auto complete box
        tk.Label(self, text="Nationality * ",font=("Calibri", 13)).grid(row=22,column=0,columnspan=2)
        nationality_entry = AutocompleteCombobox(self, textvariable=self.nationality, font=("Calibri", 13), completevalues=nationalities)
        nationality_entry.grid(row=23,column=0,columnspan=2)
        self.nationality_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.nationality_error_label.grid(row=24,column=0,columnspan=2)
        
        # Gender radiobutton
        def female():
            self.gender.set("Female")
        def male():
            self.gender.set("Male")
        tk.Label(self, text="Gender * ",font=("Calibri", 13)).grid(row=25,column=0,columnspan=2)
        tk.Radiobutton(self, text="Female", value="Female", variable=self.gender, font=("Calibri",14), command = female).grid(row=26, column=0)
        tk.Radiobutton(self, text="Male", value="Male", variable=self.gender, font=("Calibri",14), command=male()).grid(row=26, column=1)

        # Phone number entry
        tk.Label(self, text="Phone number * ",font=("Calibri", 13)).grid(row=27,column=0,columnspan=2)
        phone_number_entry = tk.Entry(self, textvariable=self.phone_number, font=("Calibri", 13))
        phone_number_entry.grid(row=28,column=0,columnspan=2)
        self.phone_number_error_label = tk.Label(self, text="", font=("Calibri", 10), fg="red")
        self.phone_number_error_label.grid(row=29,column=0,columnspan=2)
        
        # Final Registration button
        tk.Label(self, text="").grid(row=30,column=0,columnspan=2)
        registration_button = tk.Button(self, text="Register", width=10, height=1, command=lambda: register_user(register_data, entries, error_labels),font=("Calibri", 13))
        registration_button.grid(row=31,column=0,columnspan=2)
        
        
        # Create all necessary lists
        # 
        register_data = [self.username, self.password, self.password_confirmation, self.name, self.surname, self.email, self.age, self.nationality, self.phone_number, self.gender]       # gender deleted
        infos = []

        # list of all entry widgets --- they are global, so without 'self.'  
        entries = [username_entry, password_entry, password_confirmation_entry, name_entry, surname_entry, email_entry, age_entry, nationality_entry, phone_number_entry]


        #list of all error labels --- labels below entries to show warnings and errors    
        error_labels =[self.username_error_label, self.password_error_label, self.password_confirmation_error_label, self.name_error_label, self.surname_error_label, self.email_error_label, self.age_error_label, self.nationality_error_label, self.phone_number_error_label] 


    


        # Binding functions     -   maybe try to do it as another function
        # if entry clicked - Clear red highlight color of unproperly filed entrie
        username_entry.bind("<FocusIn>",username_color_white)
        password_entry.bind("<FocusIn>", lambda event: password_color_white(event))
        password_confirmation_entry.bind("<FocusIn>",password_confirmation_color_white)
        name_entry.bind("<FocusIn>",name_color_white)
        surname_entry.bind("<FocusIn>",surname_color_white)
        email_entry.bind("<FocusIn>",email_color_white)
        age_entry.bind("<FocusIn>",age_color_white)
        phone_number_entry.bind("<FocusIn>",phone_number_color_white)




