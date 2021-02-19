'''
This file creates datasets of all orders of size
using the original real datasets found on the internet.
'''

import os
import csv
from math import log10, floor, ceil
from random import sample, uniform

max_range = 7

# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

filenames = os.listdir( './formatted_CSVs' )


for name in filenames:  # for each real dataset
    print(name)

    # read contents of file
    with open('./formatted_CSVs/' + name, 'r') as csvfile:   
        list_of_tuples = [tuple([float(i) for i in line]) for line in csv.reader(csvfile)]
        size = len(list_of_tuples)

        # perform downsampling if needed
        print('down')
        level = floor(log10(size))
        while level >= 1:
            print(level)
            # create smaller datasets by down-sampling
            new_down_list = sample(list_of_tuples, 10**level)
            with open('./Internet_Datasets/set_' + str(level) + '/' + name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for point in new_down_list:
                    writer.writerow(point)
            # decrease level
            level = level - 1
        
        # perform upsampling if needed
        print('up')
        level = ceil(log10(size))
        while level < max_range:
            print(level)
            # create bigger datasets by over-sampling
            new_up_list = []
            for point in list_of_tuples:
                new_up_list.append(point)
                for _ in range(1, (10**level)//size):
                    x_new = uniform(point[0] - 1, point[0] + 1)
                    y_new = uniform(point[1] - 1, point[1] + 1)
                    new_up_list.append((x_new, y_new))
            with open('./Internet_Datasets/set_' + str(level) + '/' + name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for point in new_up_list:
                    writer.writerow(point)
            # increase level
            level = level + 1
