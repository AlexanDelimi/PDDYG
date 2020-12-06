'''
Create KD Tree with 2 dimenions.
Use whole list of points, sort by dimension and insert median element.
This gives a perfectly balanced binary tree.
The tree is eventually stored as a dictionary.
'''

from operator import itemgetter
from pprint import pprint

class Node():

    def __init__(self, point, left_child, right_child):
        self.point = point
        self.left_child = left_child
        self.right_child = right_child

    def to_dict(self):
        
        dictionary = {
            'point': self.point,
            'left child': None,
            'right child': None
        }
        
        if self.left_child != None:
            dictionary['left child'] = self.left_child.to_dict()
        
        if self.right_child != None:
            dictionary['right child'] = self.right_child.to_dict()
        
        return dictionary
 

def kdtree(point_list, dimensions, depth: int = 0):
    
    if len(point_list) == 0:
        return None
    
    axis = depth % dimensions               # select axis based on depth
    point_list.sort(key=itemgetter(axis))   # sort point list by axis
    median = len(point_list) // 2           # index of median point

    # create node and construct subtrees
    return Node(

        point=point_list[median],

        left_child=kdtree(point_list=point_list[:median], 
                          dimensions=dimensions, 
                          depth=depth + 1),

        right_child=kdtree(point_list=point_list[median + 1 :], 
                           dimensions=dimensions, 
                           depth=depth + 1)
    )


def main():
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    tree = kdtree(point_list=point_list, 
                  dimensions=len(point_list[0])
                  ).to_dict()
    pprint(tree)  # the print order is a little bit crazy but okay


if __name__ == "__main__":
    main()