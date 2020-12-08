'''
Create KD Tree with 2 dimenions.
Insert elements serially.
The tree is eventually stored as a dictionary.

The code was based on
https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/kdtrees.pdf
https://www.geeksforgeeks.org/k-dimensional-tree/
'''

from pprint import pprint
from node_class import Node


def insert_point(root, new_point, dims, depth):
    
    axis = depth % dims               # select axis based on depth
    
    if root is None:
        root = Node(new_point, None, None)
    
    elif root.point == new_point:
        print('Duplicate: ' + str(new_point))
    
    elif new_point[axis] < root.point[axis]:
        root.left_child = insert_point(root.left_child, new_point, 2, depth+1)
    else:
        root.right_child = insert_point(root.right_child, new_point, 2, depth+1)
    
    return root


def kdtree_serial(root, point_list, dimensions):
    for point in point_list:
        root = insert_point(root, point, dimensions, 0)
    return root


def main():
    point_list = [(2, 3), (7, 2), (5, 4), (9, 6), (4, 7), (8, 1)]
    dims = len(point_list[0])
    tree = kdtree_serial(None, point_list, dims)
    pprint(tree.to_dict())  # the print order is a little bit crazy but okay


if __name__ == "__main__":
    main()