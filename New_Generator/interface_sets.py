import os
import re
import csv
import tkinter as tk
from random import uniform
from tkinter import simpledialog, messagebox, filedialog

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

def csv_to_rects(csv_name):
    with open('./Distributions/CSVs/' + csv_name +'.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_area = 0
        rects = []
        for row in reader:
            rect = {
                'x_min': float(row['x_min']),
                'x_max': float(row['x_max']),
                'y_min': float(row['y_min']),
                'y_max': float(row['y_max'])
                }
            total_area += ( rect['x_max'] - rect['x_min'] ) * ( rect['y_max'] - rect['y_min'] )
            rects.append(rect)
    
    return rects, total_area


def distribution_to_points(csv_name, set_number):

    # create new points csv file
    with open('./Datasets/set_' + str(set_number) + '/' + csv_name + '.csv' , newline='', mode='w') as datafile:
        data_writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # retrive rectangles
        rects, total_area = csv_to_rects(csv_name)

        for rect in rects:
            # calculate number of points based on rectangle area percentage
            rect_area = abs( rect['x_max'] - rect['x_min'] ) * abs( rect['y_max'] - rect['y_min'] )
            num_points = int( (10**set_number) * rect_area / total_area )

            for _ in range(num_points):
                # create new point in rectangle
                x = uniform(rect['x_min'], rect['x_max'])
                y = uniform(rect['y_min'], rect['y_max'])
                # write new point to points csv file
                data_writer.writerow([x, y])


if __name__ == '__main__':
    
    root = tk.Tk() 
    root.withdraw()

    distr_dir = os.path.join(dirname, 'Distributions', 'CSVs')

    create_sets = tk.messagebox.askquestion('', ' C R E A T E')

    if create_sets == 'yes':
    
        # open directory dialog to get the distribution csv files
        filepaths = list(filedialog.askopenfilenames(initialdir=distr_dir))
        
        for path in filepaths:
            if 'Distributions' in path:
                # strip the directory to keep only the distribution csv file name
                csv_name = re.findall('distr_[0-9]+', path)[0]

                for set_number in range(1,7):
                    # create points csv file in each set folder
                    distribution_to_points(csv_name, set_number)
                    
    
    elif create_sets == 'no':

        delete_sets = tk.messagebox.askquestion('', ' D E L E T E')

        if delete_sets == 'yes':

            # open directory dialog to get the distribution csv files
            filepaths = list(filedialog.askopenfilenames(initialdir=distr_dir))
            
            for path in filepaths:
                    if 'Distributions' in path:

                        for set_number in range(1,7):
                            # delete corresponding points csv files from all sets
                            os.remove(re.sub('Distributions/CSVs', 'Datasets/set_' + str(set_number), path))
