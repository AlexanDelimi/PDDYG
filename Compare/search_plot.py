import matplotlib.pyplot as plt
import json
import os
import re

# set directory at file location again
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

max_range = 7
trees = ['KdTree', 'QuadTree', 'RangeTree']
symbol = { 'KdTree': 'r-o', 'QuadTree': 'g-*', 'RangeTree': 'b-s'}
num_neighbors = [1, 5, 10, 25, 50, 100, 250, 500]

origin = 'fake' # 'fake' or 'real'

if origin == 'fake':
    with open('./search.json', 'r') as f:
        search_results = json.load(f)
elif origin == 'real':
    with open('./real_search.json', 'r') as f:
        search_results = json.load(f)


_, axs = plt.subplots(2, 3)

for i in range(1,max_range):

    for tree in trees:

        for target in ['inner', 'outter']:

            axs[i//4, (i-1)%3].plot(num_neighbors, 
                                    [ search_results[str(i)][tree][str(k)][target] for k in num_neighbors ],
                                    symbol[tree] if target == 'inner' else re.sub('-','--', symbol[tree]), 
                                    label=tree)
            # axs[i//4, (i-1)%3].plot(num_neighbors, 
            #                         [ log10( results[str(i)][func][str(k)] + 10**0.001 ) for k in num_neighbors ],
            #                         symbol[func], 
            #                         label=func)
            axs[i//4, (i-1)%3].set_title('10^' + str(i) + ' points')
            axs[i//4, (i-1)%3].legend()

plt.show()