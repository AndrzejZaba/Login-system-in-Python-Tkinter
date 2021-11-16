import re
from tkinter import *  
from tkinter import ttk  
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
import os
import re                                   # generally for checking if specific character is or is not included in string
from entries_validation import *

# nationalities list is in entries_validation_functions.py file



# First screen of the program. 
def account_window(screen):

    screen.title("Account")
    screen.geometry("300x250")
    Label(screen, text="Flight search", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label().pack()
    Button(screen,text="Login", width="30", command=lambda:login_window(screen), pady=10).pack()
    Label().pack()
    Button(screen, text="Register", width="30", command=lambda:register_window(screen), pady=10).pack()
    

# Happens when the sign-in procedure is complete --- username and password are correct 
def login_success(login_screen):
    login_screen.destroy()
    try:
        registration_window.destroy()
    except:
        print("")
    print("SUCCES!")

    
def password_not_recognised():
    messagebox.showerror("Wrong password","Wrong password, try again.")


def user_not_found():
    messagebox.showerror("Wrong username","User not found, try another username.")


# Verification of given username and password
def login_verify(username_to_verify, password_to_verify, username_entry, password_entry, login_screen):
    username = username_to_verify.get()
    password = password_to_verify.get()

    username_entry.delete(0,END)
    password_entry.delete(0,END)


    list_of_files = os.listdir("Users/")
    if username in list_of_files:
        file1 = open("Users/"+username, "r")
        verify = file1.read().splitlines()
        if password == verify[1]:
            print("login success")
            login_success(login_screen)
        else:
            print("password has not been recognized")
            password_not_recognised()
    else:
        print("User not found")
        user_not_found()


# Window with log in form
def login_window(m_screen):
    
    login_screen = Toplevel(m_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")

    Label(login_screen, text="Please enter your details below: ", pady=10, font=("Calibri", 15)).pack()
    Label(login_screen).pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ", font=("Calibri", 13)).pack()
    username_entry_log = Entry(login_screen, textvariable=username_verify,font=("Calibri", 13))
    username_entry_log.pack()

    Label(login_screen, text="Password * ", font=("Calibri", 13)).pack()
    password_entry_log = Entry(login_screen, textvariable=password_verify,font=("Calibri", 13))
    password_entry_log.pack()

    Label(login_screen).pack()
    Button(login_screen, text="Login", command=lambda: login_verify(username_verify, password_verify, username_entry_log, password_entry_log, login_screen),pady=5,padx=15,font=("Calibri", 12)).pack()



def register_user(register_data, entries, error_labels, registration_window):
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
            entries[number].delete(0,END)
        file.write(infos[len(infos)-1])
        file.close
        registration_window.destroy()




# Binding functions
def username_color_white(event):
    username_entry.configure(bg="#ffffff")
def password_color_white(event, label):
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
def register_window(m_screen):
    # Try to remove register window as a global variable
    # maybe through making all, account window, login window and register window in the same screen, not as a Toplevel
    global registration_window 
    registration_window = Toplevel(m_screen)
    registration_window.title("Registration form")
    registration_window.geometry("300x850")

    global username, password, username_entry, password_entry, password_confirmation, password_confirmation_entry, email, email_entry, age, age_entry, name, name_entry, surname, surname_entry,nationality, nationality_entry, gender, phone_number, phone_number_entry            # Add remained to the registration form!!!
    username = StringVar()
    password = StringVar()
    password_confirmation = StringVar()
    name = StringVar()
    surname = StringVar()
    email = StringVar()
    nationality = StringVar()
    gender = StringVar()
    gender.set("Female")
    phone_number = StringVar()
    age = StringVar()


    Label(registration_window, text="Please enter your details below: ", pady=10, font=("Calibri", 15)).grid(row=0, column=0,columnspan=2)

    # Username entry
    label = Label(registration_window, text="Username * ", font=("Calibri", 13)).grid(row=1,column=0,columnspan=2)
    username_entry = Entry(registration_window, textvariable=username, font=("Calibri", 13),)
    username_entry.grid(row=2,column=0,columnspan=2)
    username_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    username_error_label.grid(row=3,column=0,columnspan=2)

    # Password entry
    Label(registration_window, text="Password * ",font=("Calibri", 13)).grid(row=4,column=0,columnspan=2)
    password_entry = Entry(registration_window, textvariable=password, font=("Calibri", 13), show="*")
    password_entry.grid(row=5,column=0,columnspan=2)
    password_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    password_error_label.grid(row=6,column=0,columnspan=2)

    # Password confirmation entry
    Label(registration_window, text="Confirm password * ",font=("Calibri", 13)).grid(row=7,column=0,columnspan=2)
    password_confirmation_entry = Entry(registration_window, textvariable=password_confirmation, font=("Calibri", 13), show="*")
    password_confirmation_entry.grid(row=8,column=0,columnspan=2)
    password_confirmation_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    password_confirmation_error_label.grid(row=9,column=0,columnspan=2)

    # Name entry
    Label(registration_window, text="Name * ",font=("Calibri", 13)).grid(row=10,column=0,columnspan=2)
    name_entry = Entry(registration_window, textvariable=name, font=("Calibri", 13))
    name_entry.grid(row=11,column=0,columnspan=2)
    name_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    name_error_label.grid(row=12,column=0,columnspan=2)

    # Surname entry
    Label(registration_window, text="Surname * ",font=("Calibri", 13)).grid(row=13,column=0,columnspan=2)
    surname_entry = Entry(registration_window, textvariable=surname, font=("Calibri", 13))
    surname_entry.grid(row=14,column=0,columnspan=2)
    surname_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    surname_error_label.grid(row=15,column=0,columnspan=2)

    # Email entry
    Label(registration_window, text="Email * ",font=("Calibri", 13)).grid(row=16,column=0,columnspan=2)
    email_entry = Entry(registration_window, textvariable=email, font=("Calibri", 13))
    email_entry.grid(row=17,column=0,columnspan=2)
    email_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    email_error_label.grid(row=18,column=0,columnspan=2)

    # Age entry
    Label(registration_window, text="Age * ",font=("Calibri", 13)).grid(row=19,column=0,columnspan=2)
    age_entry = Entry(registration_window, textvariable=age, font=("Calibri", 13))
    age_entry.grid(row=20,column=0,columnspan=2)
    age_entry.delete(0,END)
    age_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    age_error_label.grid(row=21,column=0,columnspan=2)
    
    # Nationality - auto complete box
    Label(registration_window, text="Nationality * ",font=("Calibri", 13)).grid(row=22,column=0,columnspan=2)
    nationality_entry = AutocompleteCombobox(registration_window, textvariable=nationality, font=("Calibri", 13), completevalues=nationalities)
    nationality_entry.grid(row=23,column=0,columnspan=2)
    nationality_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    nationality_error_label.grid(row=24,column=0,columnspan=2)
    
    # Gender radiobutton
    def female():
        gender.set("Female")
    def male():
        gender.set("Male")
    Label(registration_window, text="Gender * ",font=("Calibri", 13)).grid(row=25,column=0,columnspan=2)
    Radiobutton(registration_window, text="Female", value="Female", variable=gender, font=("Calibri",14), command = female).grid(row=26, column=0)
    Radiobutton(registration_window, text="Male", value="Male", variable=gender, font=("Calibri",14), command=male()).grid(row=26, column=1)

    # Phone number entry
    Label(registration_window, text="Phone number * ",font=("Calibri", 13)).grid(row=27,column=0,columnspan=2)
    phone_number_entry = Entry(registration_window, textvariable=phone_number, font=("Calibri", 13))
    phone_number_entry.grid(row=28,column=0,columnspan=2)
    phone_number_error_label = Label(registration_window, text="", font=("Calibri", 10), fg="red")
    phone_number_error_label.grid(row=29,column=0,columnspan=2)
    
    # Final Registration button
    Label(registration_window, text="").grid(row=30,column=0,columnspan=2)
    registration_button = Button(registration_window, text="Register", width=10, height=1, command=lambda: register_user(register_data, entries, error_labels, register_window),font=("Calibri", 13))
    registration_button.grid(row=31,column=0,columnspan=2)
    
    
    # Create all necessary lists
    # 
    register_data = [username, password, password_confirmation, name, surname, email, age, nationality, phone_number, gender]       # gender deleted
    infos = []

    # list of all entry widgets   
    entries = [username_entry, password_entry, password_confirmation_entry, name_entry, surname_entry, email_entry, age_entry, nationality_entry, phone_number_entry]


    #list of all error labels --- labels below entries to show warnings and errors    
    error_labels =[username_error_label, password_error_label, password_confirmation_error_label, name_error_label, surname_error_label, email_error_label, age_error_label, nationality_error_label, phone_number_error_label] 


    


    # Binding functions     -   maybe try to do it as another function
    # if entry clicked - Clear red highlight color of unproperly filed entrie
    username_entry.bind("<FocusIn>",username_color_white)
    password_entry.bind("<FocusIn>", lambda event: password_color_white(event,password_error_label))
    password_confirmation_entry.bind("<FocusIn>",password_confirmation_color_white)
    name_entry.bind("<FocusIn>",name_color_white)
    surname_entry.bind("<FocusIn>",surname_color_white)
    email_entry.bind("<FocusIn>",email_color_white)
    age_entry.bind("<FocusIn>",age_color_white)
    phone_number_entry.bind("<FocusIn>",phone_number_color_white)




