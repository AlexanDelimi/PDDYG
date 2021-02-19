''' 
This file plots the build times of the trees.
By setting the variable 'origin' we can plot the build times
on the fake datasets or on the real datasets.
'''

import matplotlib.pyplot as plt
import json
import os

# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


origin = 'Fake' # 'Fake' or 'Real' datasets

# load build times from json according to origin
if origin == 'Fake':
    with open('./build_fake.json', 'r') as f:
        build_results = json.load(f)
elif origin == 'Real':
    with open('./build_real.json', 'r') as f:
        build_results = json.load(f)


trees = ['KdTree', 'QuadTree', 'RangeTree']
symbol = { 'KdTree': '-o', 'QuadTree': '-*', 'RangeTree': '-s'}

_, ax = plt.subplots()

# plot build times from loaded json
for tree in trees:
    plt.plot(build_results.keys(), 
            [ build_results[str(i)][tree] / (10**9) for i in build_results.keys() ],
            symbol[tree], 
            label=tree)

ax.set_title('Build Times for ' + origin + ' Distributions')
ax.set_ylabel('time (sec)')
ax.set_xlabel('base 10 logarithmic number of points')
ax.legend()

plt.show()