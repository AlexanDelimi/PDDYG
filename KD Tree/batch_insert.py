'''
Create KD Tree with 2 dimenions.
Use whole list of points, sort by dimension and insert median element.
This gives a perfectly balanced binary tree.
The tree is eventually stored as a dictionary.
'''

from operator import itemgetter
from pprint import pprint
from node_class import Node


def kdtree_batch(point_list, dimensions, depth: int = 0):
    
    if len(point_list) == 0:
        return None
    
    axis = depth % dimensions               # select axis based on depth
    point_list.sort(key=itemgetter(axis))   # sort point list by axis
    
    median = len(point_list) // 2           # index of median point

    # create node and construct subtrees
    return Node(

        point=point_list[median],

        left_child=kdtree_batch(point_list=point_list[:median], 
                                dimensions=dimensions, 
                                depth=depth + 1),

        right_child=kdtree_batch(point_list=point_list[median + 1 :], 
                                 dimensions=dimensions, 
                                 depth=depth + 1)
    )


def main():
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    tree = kdtree_batch(point_list=point_list, dimensions=len(point_list[0]))
    pprint(tree.to_dict())  # the print order is a little bit crazy but okay


if __name__ == "__main__":
    main()