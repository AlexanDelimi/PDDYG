import os
from pprint import pprint
import json


# set directory at file location again
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

origin = 'fake' # 'fake' or 'real'


search_results = {}

for i in range(min_range,max_range):
    print(str(i))

    search_results[str(i)] = {}

    for tree in trees:
        print('\t' + tree)

        search_results[str(i)][tree] = {}
                
        for k in num_neighbors:
            print('\t\t' + str(k))
            search_results[str(i)][tree][str(k)] = { 'inner': 0, 'outter': 0}
                    

pprint(search_results)

if origin == 'fake':
    with open('./search_fake.json', 'w') as f:
        json.dump(search_results, f)
elif origin == 'real':
    with open('./search_real.json', 'w') as f:
        json.dump(search_results, f)
