'''
By running this file 
we can choose a dataset and visualize it.
'''

import os
import csv
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import simpledialog, messagebox, filedialog


def points_csv_to_list_of_tuples(csv_file):
    with open(csv_file) as f:
        list_of_tuples = [tuple([float(i) for i in line]) for line in csv.reader(f)]
        return list_of_tuples


if __name__ == '__main__':

    root = tk.Tk() 
    root.withdraw()

    # open directory dialog to get the dataset csv file
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)
    
    # ask to choose file
    filepath = filedialog.askopenfilename(initialdir=os.path.join(dirname,'Datasets'))

    #convert points from csv to list of tuples
    list_of_tuples = points_csv_to_list_of_tuples(filepath)

    # plot points from csv
    plt.scatter(*zip(*list_of_tuples))
    plt.show()