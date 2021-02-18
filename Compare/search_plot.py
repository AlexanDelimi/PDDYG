import matplotlib.pyplot as plt
import json
import os
import re

# set directory at file location again
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

min_range = 1
max_range = 7
trees = ['KdTree', 'QuadTree', 'RangeTree']
symbol = { 'KdTree': 'r-o', 'QuadTree': 'g-*', 'RangeTree': 'b-s'}
num_neighbors = [1, 5, 10, 25, 50, 100, 200]

origin = 'real' # 'fake' or 'real'

if origin == 'fake':
    with open('./search_fake.json', 'r') as f:
        search_results = json.load(f)
elif origin == 'real':
    with open('./search_real.json', 'r') as f:
        search_results = json.load(f)


_, axs = plt.subplots(2, 3)

for i in range(min_range, max_range):

    for tree in trees:

        for target in ['inner', 'outter']:

            axs[i//4, (i-1)%3].plot([k for k in num_neighbors if k <= 10**i], 
                                    [ search_results[str(i)][tree][str(k)][target] / (10**9) for k in num_neighbors if k <= 10**i],
                                    symbol[tree] if target == 'inner' else re.sub('-','--', symbol[tree]), 
                                    label=tree)
            # axs[i//4, (i-1)%3].plot(num_neighbors, 
            #                         [ log10( results[str(i)][func][str(k)] + 10**0.001 ) for k in num_neighbors ],
            #                         symbol[func], 
            #                         label=func)
            axs[i//4, (i-1)%3].set_title('Search Times for Real Distributions of 10^' + str(i) + ' points')
            axs[i//4, (i-1)%3].legend()
            axs[i//4, (i-1)%3].set_xticks([k for k in num_neighbors if k <= 10**i])
            axs[i//4, (i-1)%3].set_ylabel('time (sec)')
            axs[i//4, (i-1)%3].set_xlabel('number of neighbors')

plt.show()