from tkinter import *  
from entries_validation_functions import *



def check_entries(infos, entries, error_labels, validation_table):
    
    display_text = StringVar()
    

    for index in range(0, len(infos)):
        if index == 0:
            validation_table[index] = username_validation(infos[index], entries[index], error_labels[index], display_text)
        if index == 1:
            validation_table[index] = password_validation(infos[index], entries[index], error_labels[index], display_text)
        if index == 2:
            validation_table[index] = password_confirmation_validation(infos[index], entries[index], error_labels[index], display_text, infos[index-1])
        if index == 3 or index == 4:
            validation_table[index] = name_or_surname_validation(infos[index], entries[index], error_labels[index], display_text, index)
        if index == 5:
            validation_table[index] = email_validation(infos[index], entries[index], error_labels[index], display_text)
        if index == 6:
            validation_table[index] = age_validation(infos[index], entries[index], error_labels[index], display_text)
        if index == 7:
            validation_table[index] = nationality_validation(infos[index], entries[index], error_labels[index], display_text)
        if index == 8:
            validation_table[index] = phone_number_validation(infos[index], entries[index], error_labels[index], display_text)
        

    return validation_table

            


