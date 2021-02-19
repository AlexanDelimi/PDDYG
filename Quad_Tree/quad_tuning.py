''' This file was used to find the best function 
to use as the maximum capacity of the Quad Tree nodes.
The best function would perform the fastest knn queries.
The search times are stored in search_times.json file.
'''

from QuadTree import QuadTree
from random import uniform
from math import sqrt, log
from time import process_time_ns
import json
import matplotlib.pyplot as plt


thres_funcs = ['log10(x)', 'log4(x)']
num_neighbors = [1, 5, 10, 25, 50, 100, 250, 500]
symbol = {  'log10(x)': '-o', 'log4(x)': '-*'}
target_points = [   (167,833), (500,833), (833,833),
                    (167,500), (500,500), (833,500),
                    (167,167), (500,167), (833,167)  ]


def store_search_times(file):
    '''
    Build Quad Trees of different sizes
    using log4 and log10 as capacity functions
    and store the knn search times in file.
    '''
    
    thres = {}
    results = {}

    for i in range(1, 7):   # for each size order
        print(i)
        
        # create random points
        x = 10**i
        points = [(uniform(0, 1000), uniform(0, 1000)) for _ in range(x)]
        
        # calculate capacities
        thres['log10(x)'] = i
        thres['log4(x)'] = log(x, 4)

        results[str(i)] = {}
    
        for func in thres_funcs:    # for each capacity function
            print('\t' + func)

            # build Quad Tree
            qtree = QuadTree(thres[func], points)

            results[str(i)][func] = {}

            for k in num_neighbors:     # for each number of neighbors
                print('\t\t' + str(k))

                # count elapsed time for all targets
                start = process_time_ns()
                for target in target_points:    # for each target point
                    _ = qtree.k_nn(target, k)
                elapsed = process_time_ns() - start

                # keep the average time
                results[str(i)][func][str(k)] = elapsed // 9

    # store the results in file
    with open(file, 'w') as f:
        json.dump(results, f)


def plot_search_times(file):
    '''
    Plot the search times stored in file.
    '''

    with open(file, 'r') as f:
        results = json.load(f)

        _, axs = plt.subplots(2, 3)

        for i in range(1,7):

            for func in thres_funcs:

                axs[i//4, (i-1)%3].plot(num_neighbors, 
                                        [ results[str(i)][func][str(k)] / (10**6) for k in num_neighbors ],
                                        symbol[func], 
                                        label=func)

                axs[i//4, (i-1)%3].set_title('10^' + str(i) + ' points')
                axs[i//4, (i-1)%3].set_ylabel('time (msec)')
                axs[i//4, (i-1)%3].set_xlabel('number of neighbors')
                axs[i//4, (i-1)%3].legend()
        
        plt.show()


if __name__=='__main__':
    
    file = './Quad_Tree/search_times.json'
    # store_search_times(file)
    plot_search_times(file)
