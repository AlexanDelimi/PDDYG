'''
The code for plotting is based on this web page
https://salzis.wordpress.com/2014/06/28/kd-tree-and-nearest-neighbor-nn-search-2d-case/ .
We create the tree using 'kdtree' function from 'wiki_based_code.py'
and use the functions 'plot_figure' and 'plot_tree' to visualize the kd tree.
'''

from wiki_based_code import kdtree
from pprint import pprint
from operator import itemgetter
import matplotlib.pyplot as plt
 
# line width for visualization of K-D tree
line_width = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.3]
 
def plot_tree(tree, min_x, max_x, min_y, max_y, prev_node, branch, dimensions, depth=0):

    # tree          (sub)tree to be plotted
    # prev_node     parent node
    # branch        True if (sub)tree is left child of parent node, 
    #               False if (sub)tree is right child of parent node
 
    cur_node = tree['point']
    left_branch = tree['left child']
    right_branch = tree['right child']
 
    # set line's width depending on tree's depth
    if depth > len(line_width)-1:
        ln_width = line_width[len(line_width)-1]
    else:
        ln_width = line_width[depth]
    
    axis = depth % dimensions
 
    # draw a vertical splitting line
    if axis == 0:
 
        if branch is not None and prev_node is not None:
 
            if branch:
                max_y = prev_node[1]
            else:
                min_y = prev_node[1]
 
        plt.plot([cur_node[0],cur_node[0]], [min_y,max_y], linestyle='-', color='red', linewidth=ln_width)
 
    # draw a horizontal splitting line
    elif axis == 1:
 
        if branch is not None and prev_node is not None:
 
            if branch:
                max_x = prev_node[0]
            else:
                min_x = prev_node[0]
 
        plt.plot([min_x,max_x], [cur_node[1],cur_node[1]], linestyle='-', color='blue', linewidth=ln_width)
 
    # draw the current node
    plt.plot(cur_node[0], cur_node[1], 'ko')
 
    # draw left and right branches of the current node
    if left_branch is not None:
        plot_tree(left_branch, min_x, max_x, min_y, max_y, cur_node, True, dimensions, depth+1)
 
    if right_branch is not None:
        plot_tree(right_branch, min_x, max_x, min_y, max_y, cur_node, False, dimensions, depth+1)


def plot_figure(kd_tree, dimensions, min_val, max_val, delta):
    plt.figure("K-d Tree")
    plt.axis( [min_val-delta, max_val+delta, min_val-delta, max_val+delta] )
    
    plt.grid(b=True, which='major', color='0.75', linestyle='--')
    plt.xticks([i for i in range(min_val-delta, max_val+delta, 1)])
    plt.yticks([i for i in range(min_val-delta, max_val+delta, 1)])
    
    # draw the tree
    plot_tree(tree= kd_tree, 
              min_x= min_val-delta, 
              max_x= max_val+delta, 
              min_y= min_val-delta, 
              max_y= max_val+delta, 
              prev_node= None,
              branch= None,
              dimensions= dimensions)
    
    plt.title('K-D Tree')
    plt.show()
    plt.close()


def main():
    
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    dims = len(point_list[0])

    min_val = min(min(point_list, key=itemgetter(0))[0],min(point_list, key=itemgetter(1))[1])
    max_val = max(max(point_list, key=itemgetter(0))[0],max(point_list, key=itemgetter(1))[1])
    delta = 2

    kd_tree = kdtree(point_list, dims).to_dict()
    pprint(kd_tree)  # the print order is a little bit crazy but okay

    plot_figure(kd_tree, dims, min_val, max_val, delta)


if __name__ == "__main__":
    main()