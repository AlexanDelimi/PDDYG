''' 
This file plots the search times of the trees.
By setting the variable 'origin' we can plot the search times
on the fake datasets or on the real datasets.
'''

import matplotlib.pyplot as plt
import json
import os
import re

# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


min_range = 1
max_range = 7
trees = ['KdTree', 'QuadTree', 'RangeTree']
symbol = { 'KdTree': 'r-o', 'QuadTree': 'g-*', 'RangeTree': 'b-s'}
num_neighbors = [1, 5, 10, 25, 50, 100, 200]

origin = 'Fake' # 'Fake' or 'Real'

# load search times from json according to origin
if origin == 'Fake':
    with open('./search_fake.json', 'r') as f:
        search_results = json.load(f)
elif origin == 'Real':
    with open('./search_real.json', 'r') as f:
        search_results = json.load(f)


_, axs = plt.subplots(2, 3)

for i in range(min_range, max_range):   # for each order of dataset size

    for tree in trees:      # for each tree

        for target in ['inner', 'outter']:      # for each type of target point
            
            # plot all search time diagrams
            axs[i//4, (i-1)%3].plot([k for k in num_neighbors if k <= 10**i], 
                                    [ search_results[str(i)][tree][str(k)][target] / (10**9) for k in num_neighbors if k <= 10**i],
                                    symbol[tree] if target == 'inner' else re.sub('-','--', symbol[tree]), 
                                    label=tree)
            axs[i//4, (i-1)%3].set_title('Search Times for ' + origin + ' Distributions of 10^' + str(i) + ' points')
            axs[i//4, (i-1)%3].legend()
            axs[i//4, (i-1)%3].set_xticks([k for k in num_neighbors if k <= 10**i])
            axs[i//4, (i-1)%3].set_ylabel('time (sec)')
            axs[i//4, (i-1)%3].set_xlabel('number of neighbors')

plt.show()