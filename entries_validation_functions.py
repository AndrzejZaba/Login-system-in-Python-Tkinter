from tkinter import *
import re
import requests                             # generally to check if given e-mail exhist

global nationalities
nationalities = ['Polish', 'German', "French", "British", "Swedish", "Norwegian", "Finnish", 'Duch', 'Dannish', 'Belgian', 'Spannish', 'Portugeese', 'Greek', 'Russian', 'Belarussian', 'Latwian', 'Lithuanian', 'Slovakian', 'Austrian', 'Chech', 'Italian','American', 'Mecican', 'Canadian', 'Australian']


# entry_value - value which user imput
# entry - adequate entry widget
# error_label - label widget beneth the entry widget
# display_text - text to be displayed in error label

def username_validation(entry_value, entry, error_label, display_text):
    entry.config(bg="#ffb3b3")
    if len(entry_value) == 0:
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
    elif len(entry_value) > 0 and len(entry_value) < 5:
        display_text = "Username needs to have at least 5 characters!"
        error_label.config(text=display_text)
        return 0
    else:
        display_text = ""
        error_label.config(text=display_text)
        entry.config(bg="#ffffff")
        return 1

def password_validation(entry_value, entry, error_label, display_text):
    entry.config(bg="#ffb3b3")
    if len(entry_value) == 0:
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
    elif re.search('[0-9]',entry_value) is None or re.search('[A-Z]',entry_value) is None or len(entry_value) < 8:
        display_text = "Password must contain at least: \n * 8 characters \n * one capital letter \n * one number"
        error_label.config(text=display_text)
        return 0
    else:
        display_text = ""
        error_label.config(text=display_text)
        entry.config(bg="#ffffff")
        return 1

def password_confirmation_validation(entry_value, entry, error_label, display_text, value_to_confirm):
    entry.config(bg="#ffb3b3")
    if len(entry_value) == 0:
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
    elif entry_value != value_to_confirm:
        display_text = "Passwords are not the same!"
        error_label.config(text=display_text)
        return 0
    else:
        display_text=""
        error_label.config(text=display_text)
        entry.config(bg="#ffffff")
        return 1

def name_or_surname_validation(entry_value, entry, error_label, display_text, index): # CHECK!!!!!!!
    entry.config(bg="#ffb3b3")
    if  len(entry_value) == 0:  
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
    elif re.search('[0-9]',entry_value) is not None or re.search('[\_\!\@\#\$\%\^\&\*\(\)\-\=\+\}\{\?\>\<\,\.\;\]\[\" / \\  \| ]',entry_value) is not None or len(entry_value) < 2: # UPDATE: rather works except of '\' mark         Warning!: doesn't work for special characters!!! UPDATE THIS!!!
        if index == 3:
            display_text = "Enter poper name!"
            error_label.config(text=display_text)
            return 0
        else:
            display_text = "Enter poper surname!"                   
            error_label.config(text=display_text)
            return 0
    else:
        display_text=""
        error_label.config(text=display_text)
        entry.config(bg="#ffffff")
        return 1   

def email_validation(entry_value, entry, error_label, display_text):
    entry.config(bg="#ffb3b3")
    if len(entry_value) == 0:  
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
    elif not re.search(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|pl|edu|net|gov|)', entry_value):
        display_text = "Wrong E-mail pattern!\ne.g. example@mail.com"
        error_label.config(text=display_text)
        return 0
    else:
        display_text=""
        error_label.config(text=display_text)
        entry.config(bg="#ffffff")
        return 1

def age_validation(entry_value, entry, error_label, display_text):
    entry.config(bg="#ffb3b3")
    try:
        if len(entry_value) == 0:
            display_text = "Empty field!"
            error_label.config(text=display_text)
            return 0
        elif int(entry_value) < 16:
            display_text = "You need to be at least 16 to create account"
            error_label.config(text=display_text)
            return 0
        elif len(entry_value) > 3 or int(entry_value) > 120:
            display_text = "You can not be so old!"
            error_label.config(text=display_text)
            return 0  
        else:
            display_text=""
            error_label.config(text=display_text)
            entry.config(bg="#ffffff")
            return 1
    except:
        entry.delete(0,END)
        entry_value=0
        display_text="You can not use other characters than numbers!"
        error_label.config(text=display_text)
        return 0

def nationality_validation(entry_value, entry, error_label, display_text):
    if len(entry_value) == 0:
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
    elif entry_value in nationalities:
        display_text=""
        error_label.config(text=display_text)
        return 1    
    else:
        display_text = "Choose nationality from the list!"
        error_label.config(text=display_text)
        return 0

def phone_number_validation(entry_value, entry, error_label, display_text):
    entry.config(bg="#ffb3b3")
    if len(entry_value)==0:
        display_text = "Empty field!"
        error_label.config(text=display_text)
        return 0
            
    elif re.search(r'[a-zA-Z\./?\[\] !@#$%^&*()]', entry_value):
                display_text = "number must not contain any\n letters nor special characters"
                error_label.config(text=display_text)
                return 0
    elif entry_value[0] != '+':
                display_text = "number must starts with country calling code! \n eg: \' +32\' "
                error_label.config(text=display_text)
                return 0
    elif len(entry_value) < 8:
                display_text = "Given number is too short!"
                error_label.config(text=display_text)
                return 0
    elif len(entry_value) > 14:
                display_text = "Given number is too long!"
                error_label.config(text=display_text)
                return 0

    elif re.search("\++\d{6,11}", entry_value):
                entry.config(bg="#ffffff")
                display_text = ""
                error_label.config(text=display_text)
                return 1





