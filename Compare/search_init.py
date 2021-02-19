'''
This file initializes the timers in the json file that is going to be used
by search_time.py to store the actual search times.
'''

import os
from pprint import pprint
import json


# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


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

origin = 'Fake' # 'Fake' or 'Real'


search_results = {}

for i in range(min_range,max_range):    # for each order of dataset size
    print(str(i))

    search_results[str(i)] = {}

    for tree in trees:          # for each tree type
        print('\t' + tree)

        search_results[str(i)][tree] = {}
                
        for k in num_neighbors:         # for each number of neighbors
            print('\t\t' + str(k))
            search_results[str(i)][tree][str(k)] = { 'inner': 0, 'outter': 0} # initialize timers
                    

pprint(search_results)

# store initialized timers to json according to origin
if origin == 'Fake':
    with open('./search_fake.json', 'w') as f:
        json.dump(search_results, f)
elif origin == 'Real':
    with open('./search_real.json', 'w') as f:
        json.dump(search_results, f)
