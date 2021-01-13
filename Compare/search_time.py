import os
import sys
import csv
from pprint import pprint
import matplotlib.pyplot as plt
from math import log
from time import process_time_ns
import json


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


''''''''' SIMPLE TEST '''''''''

max_range = 7
trees = ['KdTree', 'QuadTree', 'RangeTree']
num_neighbors = [1, 5, 10, 25, 50, 100, 250, 500]

inner_targets = [   (167,833), (500,833), (833,833),
                    (167,500), (500,500), (833,500),
                    (167,167), (500,167), (833,167)  ]

outter_targets = [  (-2000, 3000),  (500, 3000),  (3000, 3000),
                    (-2000, 500),                 (3000, 500),
                    (-2000, -2000), (500, -2000), (3000, -2000)  ]

origin = 'fake' # 'fake' or 'real'

# plt.scatter(*zip(*inner_targets), color='red')
# plt.scatter(*zip(*outter_targets), color='blue')
# plt.show()

search_results = {}

for i in range(1,max_range):
    print(str(i))

    search_results[str(i)] = {}

    for tree in trees:
        print('\t' + tree)

        # get all distribution csv file names
        if origin == 'fake':
            filenames = os.listdir( '../New_Generator/Distributions/CSVs' )
        elif origin == 'real':
            filenames = os.listdir( '../Internet/formatted_CSVs' )

        search_results[str(i)][tree] = {}

        for k in num_neighbors:
            print('\t\t' + str(k))

            search_results[str(i)][tree][str(k)] = { 'inner': 0, 'outter': 0}
        
            for name in filenames:
                print('\t\t\t' + name)

                if origin == 'fake':
                    csv_file = '../New_Generator/Datasets/set_' + str(i) + '/' + name
                elif origin == 'real':
                    csv_file = '../Internet/Internet_Datasets/set_' + str(i) + '/' + name

                with open(csv_file) as f:
                    
                    list_of_tuples = [tuple([float(i) for i in line]) for line in csv.reader(f)]

                    root = None

                    if tree == 'KdTree':
                        root = KdTree(list_of_tuples)

                    elif tree == 'QuadTree':
                        root = QuadTree(log(10**i, 4), list_of_tuples)

                    elif tree == 'RangeTree':
                        root = RangeTree(list_of_tuples)

                    start = process_time_ns()
                    for in_target in inner_targets:
                        _ = root.k_nn(in_target, k)  
                    elapsed = process_time_ns() - start

                    search_results[str(i)][tree][str(k)]['inner'] += elapsed / len(inner_targets)

                    start = process_time_ns()
                    for out_target in outter_targets:
                        _ = root.k_nn(out_target, k)  
                    elapsed = process_time_ns() - start

                    search_results[str(i)][tree][str(k)]['outter'] += elapsed / len(outter_targets)
                    
                    
            search_results[str(i)][tree][str(k)]['inner'] /= len(filenames)
            search_results[str(i)][tree][str(k)]['outter'] /= len(filenames)        
                                

pprint(search_results)

if origin == 'fake':
    with open('./search.json', 'w') as f:
        json.dump(search_results, f)
elif origin == 'real':
    with open('./real_search.json', 'w') as f:
        json.dump(search_results, f)
