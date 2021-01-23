from operator import itemgetter
from pprint import pprint
import matplotlib.pyplot as plt
from KdNode import KdNode
from math import sqrt, ceil, floor
from time import process_time_ns


class KdTree():
    '''
    Defines the tree by its root node
    using the points from the list of tuples provided.
    '''

    def __init__(self, point_list):
        ''' Kd Tree constructor. '''

        self.num_points = len(point_list)
        self.xmin = min(point_list, key=itemgetter(0))[0]
        self.ymin = min(point_list, key=itemgetter(1))[1]
        self.xmax = max(point_list, key=itemgetter(0))[0]
        self.ymax = max(point_list, key=itemgetter(1))[1]
        self.root = KdTree.build_kdtree(point_list, 2)

    @staticmethod
    def build_kdtree(point_list, dimensions, depth: int = 0):
        ''' Helper function for the constructor. '''
        
        if len(point_list) == 0:
            return None
        
        axis = depth % dimensions               # select axis based on depth
        point_list.sort(key=itemgetter(axis))   # sort point list by axis
        
        median = len(point_list) // 2           # index of median point

        # create node and construct subtrees
        return KdNode(

            point=point_list[median],

            left_child=KdTree.build_kdtree(point_list=point_list[:median],
                                        dimensions=dimensions, 
                                        depth=depth + 1),

            right_child=KdTree.build_kdtree(point_list=point_list[median + 1 :], 
                                        dimensions=dimensions, 
                                        depth=depth + 1)
        )
 
    def graph(self, delta=2):
        ''' Plot the tree. '''
        
        plt.figure()
        plt.axis( [self.xmin-delta, self.xmax+delta, self.ymin-delta, self.ymax+delta] )
        
        # draw the tree
        self.root.plot_tree(min_x= self.xmin-delta, 
                        max_x= self.xmax+delta, 
                        min_y= self.ymin-delta, 
                        max_y= self.ymax+delta, 
                        prev_node= None,
                        branch= None,
                        dimensions= 2)
        
        plt.title('KD Tree')
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
                    nn = KdNode.nearest_neighbor(self.root, target_point, 2, 0, nearest_list)
                    nearest_list.append(nn.point)
                
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
                nn = KdNode.nearest_neighbor(self.root, target_point, 2, 0, nearest_list)
                nearest_list.append(nn.point)
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

    def graph_knn(self, target_point, neighbors, delta=2):
        '''
        Plot the tree and the nearest neighbors around the target point.
        '''

        plt.figure()
        plt.title('KD Tree')

        # find the leaves
        points = self.root.get_points([])
        
        # draw all points stored in tree
        plt.scatter(*zip(*points))
        # draw the target point
        plt.scatter(target_point[0], target_point[1], color='black', marker='D')
        # re-draw the nearest neighbors found
        plt.scatter(*zip(*neighbors), color='red', marker='s')

        # draw circle from target point to furthest neighbor found
        radius = sqrt(KdNode.squared_distance(target_point, neighbors[-1]))
        circle = plt.Circle((target_point[0], target_point[1]), radius, facecolor='none', edgecolor='#000000')
        plt.gca().add_patch(circle)

        plt.axis( [self.xmin-delta, self.xmax+delta, self.ymin-delta, self.ymax+delta] )
        plt.show()

    def to_dict(self):
        ''' Helper function to print the tree. '''

        return self.root.to_dict()
    