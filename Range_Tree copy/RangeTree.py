import matplotlib.pyplot as plt
from math import sqrt
from operator import itemgetter
from RangeNode import RangeNode


class RangeTree():

    def __init__(self, lista):
        self.num_points = len(lista)
        self.root = RangeTree.build_2D_Range_Tree(lista)

    def to_dict(self):
        return self.root.to_dict()

    @staticmethod
    def build_2D_Range_Tree(lista):

        list_x = sorted(list(set([point[0] for point in lista])))
        root = RangeNode.build_1D_Range_Tree(list_x)
        root.insert_leaves(lista, 0)

        root.insert_bst_y(lista)              

        return root
    
    def k_nn(self, target_point, k):
        ''' Get the k nearest neighbors around target
            among of total of num_points contained in root tree. '''
        
        if k < 1:
            return [target_point]
        else:
            nearest_list = []
            while (len(nearest_list) < k) and (len(nearest_list) < self.num_points):
                nn = RangeNode.nearest_neighbor_x(self.root, target_point, nearest_list)
                nearest_list.append(nn)
            return nearest_list

    def graph(self):
        '''
        Plot the tree.
        '''
        # initialize figure
        plt.figure()
        plt.title("Range Tree")

        # find the leaves
        leaves = RangeNode.get_leaves(self.root, [])
        
        # draw all points stored in tree
        plt.scatter(*zip(*leaves))
        
        plt.show()

    def graph_knn(self, target_point, neighbors):
        '''
        Plot the tree and the nearest neighbors around the target point.
        '''
        # initialize figure
        fig = plt.figure()
        plt.title("Range Tree")
        
        # find the leaves
        leaves = RangeNode.get_leaves(self.root, [])
        
        # draw all points stored in tree
        plt.scatter(*zip(*leaves))
        # draw the target point
        plt.scatter(target_point[0], target_point[1], color='black', marker='D')
        # re-draw the nearest neighbors found
        plt.scatter(*zip(*neighbors), color='red', marker='s')

        # draw circle from target point to furthest neighbor found
        radius = sqrt(RangeNode.squared_distance(target_point, neighbors[-1]))
        circle = plt.Circle((target_point[0], target_point[1]), radius, facecolor='none', edgecolor='#000000')
        plt.gca().add_patch(circle)

        # reset axis limits
        min_val = min(min(leaves, key=itemgetter(0))[0],min(leaves, key=itemgetter(1))[1])
        max_val = max(max(leaves, key=itemgetter(0))[0],max(leaves, key=itemgetter(1))[1])
        delta = 2
        plt.axis( [min_val-delta, max_val+delta, min_val-delta, max_val+delta] )

        plt.show()
