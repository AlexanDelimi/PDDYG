'''
This file calculates and stores the build times of each tree
for every order of dataset size. By setting the variable 'origin'
we can build the trees using fake or real datasets.
'''

import os
import sys
import csv
from pprint import pprint
import matplotlib.pyplot as plt
from math import log
from time import process_time_ns
import json
import pickle
import re


''''''''' IMPORT TREES '''''''''

# When importing a file, Python only searches the current directory, the directory that the entry-point script is running from, and sys.path which includes locations such as the package installation directory. So by changing the current directory and adding it to sys.path we can import the tree files we need.

# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

# go to KD_Tree folder directory
os.chdir('../KD_Tree')
sys.path.insert(1, os.getcwd())
from KdTree import KdTree

# go to Quad_Tree folder directory
os.chdir('../Quad_Tree')
sys.path.insert(1, os.getcwd())
from QuadTree import QuadTree

# go to Range_Tree folder directory
os.chdir('../Range_Tree')
sys.path.insert(1, os.getcwd())
from RangeTree import RangeTree

# set directory at file location again
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


''''''''' MAIN CODE '''''''''

min_range = 1
max_range = 7
trees = ['KdTree', 'QuadTree', 'RangeTree']

origin = 'fake' # 'fake' or 'real'

build_results = {}  # initialization

for i in range(min_range, max_range):   # for each order of dataset size
    print(str(i))

    build_results[str(i)] = {}

    for tree in trees:      # for each tree
        print('\t' + tree)

        # get all distribution csv file names
        if origin == 'fake':
            filenames = os.listdir( '../New_Generator/Distributions_4/CSVs' )
        elif origin == 'real':
            filenames = os.listdir( '../Internet/formatted_CSVs_4' )

        build_time = 0    # initialize timer

        for name in filenames:      # for each distribution
            print('\t\t' + name)

            # load distribution from directory according to origin
            if origin == 'fake':
                csv_file = '../New_Generator/Datasets/set_' + str(i) + '/' + name
            elif origin == 'real':
                csv_file = '../Internet/Internet_Datasets/set_' + str(i) + '/' + name         

            with open(csv_file) as f:
                
                # read list of points
                list_of_tuples = [tuple([float(i) for i in line]) for line in csv.reader(f)]

                root = None

                # build the tree of the current iteration
                if tree == 'KdTree':
                    start = process_time_ns()
                    root = KdTree(list_of_tuples)
                    build_time = build_time + process_time_ns() - start

                elif tree == 'QuadTree':
                    start = process_time_ns()
                    root = QuadTree(log(10**i, 4), list_of_tuples)
                    build_time = build_time + process_time_ns() - start

                elif tree == 'RangeTree':
                    start = process_time_ns()
                    root = RangeTree(list_of_tuples)
                    build_time = build_time + process_time_ns() - start
                
                # load load from pickle (eg. set_2_KdTree_distr_5.pkl or set_2_KdTree_new_mrds.pkl)
                pickle_name = 'set_' + str(i) + '_' + tree + '_' + re.sub('.csv', '.pkl', name)

                with open('./pickle_trees/' + origin + '/' + pickle_name, 'wb') as output:
                    pickle.dump(root, output, pickle.HIGHEST_PROTOCOL)
        
        # store average build time for current order of size and current tree type
        build_results[str(i)][tree] = build_time / len(filenames)

pprint(build_results)

# store results in json according to origin
if origin == 'fake':
    with open('./build_fake.json', 'w') as f:
        json.dump(build_results, f)
elif origin == 'real':
    with open('./build_real.json', 'w') as f:
        json.dump(build_results, f)
