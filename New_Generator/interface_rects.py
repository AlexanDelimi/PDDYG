import os
import re
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

from draw_rectangles import open_interface

os.chdir('./New_Generator')

root = tk.Tk() 
root.withdraw()

new_file = tk.messagebox.askquestion('', ' C R E A T E')

if new_file == 'yes':
    
    # get all distribution csv file names in Distributions/CSVs folder
    filenames = os.listdir('./Distributions/CSVs')
    
    # strip the names to keep only the number
    numbers = []
    for name in filenames:
        number = int(re.sub('[^0-9]', '', name))
        numbers.append(number)
    numbers.sort()

    # find the smallest integer that does not exist already
    index = 0
    new_number = 1
    while index < len(numbers):
        if numbers[index] == new_number:
            index += 1
            new_number += 1
        else:
            break

    # prepare the new distribution csv file name
    new_name = 'distr_' + str(new_number)

    # create distribution csv and png files
    open_interface(new_name, edit=False)

elif new_file == 'no':

    edit_file = tk.messagebox.askquestion('', ' E D I T')

    if edit_file == 'yes':

        # open directory dialog to get the distribution csv file
        filepath = filedialog.askopenfilename(initialdir='./Distributions/CSVs')
        
        if filepath != '':
            # strip the directory to keep only the distribution csv file name
            filename = re.findall('distr_[0-9]+', filepath)[0]
            
            open_interface(filename, True)
    
    elif edit_file == 'no':

        delete_files = tk.messagebox.askquestion('', ' D E L E T E')

        if delete_files == 'yes':

            # open directory dialog to get the distribution csv files
            filepaths = list(filedialog.askopenfilenames(initialdir='./Distributions/CSVs'))
            
            for path in filepaths:
                if 'Distributions' in path:
                    # delete selected distribution csv file
                    os.remove(path)
                    # delete corresponding distribution png file
                    os.remove(re.sub('CSVs', 'PNGs', re.sub('.csv', '.png', path)))
            