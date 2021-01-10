import matplotlib.pyplot as plt
import json
import os

# set directory at file location again
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


trees = ['KdTree', 'QuadTree', 'RangeTree']
symbol = { 'KdTree': '-o', 'QuadTree': '-*', 'RangeTree': '-s'}

with open('./build.json', 'r') as f:
    build_results = json.load(f)

    _, ax = plt.subplots()

    for tree in trees:

        plt.plot(build_results.keys(), 
                [ build_results[str(i)][tree] for i in build_results.keys() ],
                symbol[tree], 
                label=tree)
        # axs[i//4, (i-1)%3].plot(num_neighbors, 
        #                         [ log10( results[str(i)][func][str(k)] + 10**0.001 ) for k in num_neighbors ],
        #                         symbol[func], 
        #                         label=func)
        ax.set_title('Build Time')
        ax.legend()
    
    plt.show()