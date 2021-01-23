import matplotlib.pyplot as plt
from math import sqrt
from operator import itemgetter
from RangeNode import RangeNode
from time import process_time_ns


class RangeTree():
    '''
    Defines the tree by its root node
    using the points from the list of tuples provided.
    '''

    def __init__(self, lista):
        ''' Quad Tree constructor. '''

        self.num_points = len(lista)
        self.root = RangeTree.build_2D_Range_Tree(lista)

    @staticmethod
    def build_2D_Range_Tree(lista):
        ''' Helper function for the constructor. '''

        # build range tree of first dimension
        list_x = sorted(list(set([point[0] for point in lista])))
        root = RangeNode.build_1D_Range_Tree(list_x)
        root.insert_leaves(lista, 0)
        # build all range trees of second dimension 
        root.insert_bst_y(lista)              

        return root

    def graph(self):
        ''' Plot the tree. '''
        
        # initialize figure
        plt.figure()
        plt.title("Range Tree")

        # find the leaves
        leaves = RangeNode.get_leaves(self.root, [])
        
        # draw all points stored in tree
        plt.scatter(*zip(*leaves))
        
        plt.show()

    def k_nn(self, target_point, k=0, timing='False'):
        '''
        Get the k nearest neighbors around target
        among the points contained in the tree. 
        '''
        
        if timing == 'False':   # perform normal knn search
            if k < 1:
                return [target_point]
            else:
                nearest_list = []
                # search until k neighbors are found or all points are reported
                while (len(nearest_list) < k) and (len(nearest_list) < self.num_points):
                    # find next nearest and add to list
                    nn = RangeNode.nearest_neighbor_x(self.root, target_point, nearest_list)
                    nearest_list.append(nn)
                
                return nearest_list
            
        elif timing == 'True':  # perform customised knn search to report the searching times

            # list of nearest neighbors
            nearest_list = []
            # different numbers of neighbors we want
            num_neighbors = [1, 5, 10, 25, 50, 100, 200]
            # timers = { number of neighbors : elapsed time }
            timers = {}
            # common starting time point
            start = process_time_ns()
            
            # search for maximum number of neighbors or until no points remain
            while (len(nearest_list) < num_neighbors[-1]) and (len(nearest_list) < self.num_points):
                # find next nearest and add to list
                nn = RangeNode.nearest_neighbor_x(self.root, target_point, nearest_list)
                nearest_list.append(nn)
                # check if we found a number of neighbors we wanted
                if len(nearest_list) in num_neighbors:
                    # keep time from common start
                    timers[str(len(nearest_list))] = process_time_ns() - start   
            
            # all points are exhausted - keep time
            final_timer = process_time_ns() - start
            # current number of found neighbors
            length = len(nearest_list)
            
            # for each number of neighbors we wanted
            for num_k in num_neighbors:
                # check if we exhausted all points before reaching an amount of neighbors we wanted
                if num_k > length:
                    # set time equal to whole time the while loop was running
                    timers[str(num_k)] = final_timer
            
            return timers

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

    def to_dict(self):
        ''' Helper function to print the tree. '''

        return self.root.to_dict()