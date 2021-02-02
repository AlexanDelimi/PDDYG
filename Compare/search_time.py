import os
import sys
from pprint import pprint
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


''''''''' SIMPLE TEST '''''''''

min_range = 1
max_range = 7
trees = ['KdTree', 'QuadTree', 'RangeTree']
num_neighbors = [1, 5, 10, 25, 50, 100, 200]

inner_targets = [   (250,750), (750,750),
                    (250,250), (750,250)
                ]

outter_targets = [                  (500, 3000),
                    (-2000, 500),                 (3000, 500),
                                    (500, -2000)
                ]

origin = 'fake' # 'fake' or 'real'

# load json file with existing search results
if origin == 'fake':
    with open('./search_fake.json', 'r') as f:
        search_results = json.load(f)
elif origin == 'real':
    with open('./search_real.json', 'r') as f:
        search_results = json.load(f)


for i in range(min_range, max_range):
    print(str(i))

    for tree in trees:
        print('\t' + tree)

        # re-initialize inner and outter values to zero before updating them
        for k in num_neighbors:
            search_results[str(i)][tree][str(k)]['inner'] = 0
            search_results[str(i)][tree][str(k)]['outter'] = 0

        # get all distribution csv file names
        if origin == 'fake':
            filenames = os.listdir( '../New_Generator/Distributions_4/CSVs' )
        elif origin == 'real':
            filenames = os.listdir( '../Internet/formatted_CSVs_4' )

        for name in filenames:
            print('\t\t' + name)

            # eg. set_2_KdTree_distr_5.pkl or set_2_KdTree_new_mrds.pkl
            pickle_name = 'set_' + str(i) + '_' + tree + '_' + re.sub('.csv', '.pkl', name)
            
            # load (any kind of) tree from pickle
            with open('./pickle_trees/' + origin + '/' + pickle_name, 'rb') as input:
                root = pickle.load(input)
                
                # get timers dictionary for inner target
                for in_target in inner_targets:
                    in_timers = root.k_nn(in_target, timing='True')
                    # add corresponding inner timers to each other
                    for k in num_neighbors:
                        search_results[str(i)][tree][str(k)]['inner'] += in_timers[str(k)]
                
                # get timers dictionary for outter target
                for out_target in outter_targets:
                    out_timers = root.k_nn(out_target, timing='True')
                    # add corresponding outter timers to each other
                    for k in num_neighbors:
                        search_results[str(i)][tree][str(k)]['outter'] += out_timers[str(k)] 
                
        # average inner and outter timers between targets and distributions
        for k in num_neighbors:
            search_results[str(i)][tree][str(k)]['inner'] /= (len(inner_targets) * len(filenames))
            search_results[str(i)][tree][str(k)]['outter'] /= (len(outter_targets) * len(filenames))


# store json file with updated search results
if origin == 'fake':
    with open('./search_fake.json', 'w') as f:
        json.dump(search_results, f)
elif origin == 'real':
    with open('./search_real.json', 'w') as f:
        json.dump(search_results, f)
