import matplotlib.pyplot as plt
import matplotlib.patches as patches
from operator import itemgetter
from QuadNode import QuadNode
from time import process_time_ns

class QuadTree:
    '''
    Defines the tree by its root node
    using the points from the list of tuples provided
    while storing up to k points inside a leaf.
    '''

    def __init__(self, k, points):
        ''' Quad Tree constructor. '''

        self.threshold = k
        self.num_points = len(points)
        xmin = min(points, key=itemgetter(0))[0]
        ymin = min(points, key=itemgetter(1))[1]
        xmax = max(points, key=itemgetter(0))[0]
        ymax = max(points, key=itemgetter(1))[1]
        width = xmax - xmin
        height = ymax - ymin
        self.root = QuadNode(xmin - 0.01, ymin - 0.01, width + 0.02, height + 0.02)
        self.root.subdivide(self.threshold, points)

    def graph(self):
        ''' Plot the tree. '''

        # initialize figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title("Quad Tree")

        # find the deepest nodes and their leaves
        children, leaves = self.root.find_children([], [])
        for node in children:
            ax.add_patch(patches.Rectangle((node.x, node.y), node.width, node.height, fill=False))
        
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
                # invalid neighbors were asked
                return [target_point]
            else:
                nearest_list = []
                # search until k neighbors are found or all points are reported
                while (len(nearest_list) < k) and (len(nearest_list) < self.num_points):
                    # find next nearest and add to list
                    nn = self.root.nearest_neighbor(target_point, nearest_list)
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
                nn = self.root.nearest_neighbor(target_point, nearest_list)
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
        ax = fig.add_subplot(111)
        plt.title("Quad Tree")
        
        # find the deepest nodes and their leaves
        children, leaves = self.root.find_children([], [])
        for node in children:
            ax.add_patch(patches.Rectangle((node.x, node.y), node.width, node.height, fill=False))
        
        # draw all points stored in tree
        plt.scatter(*zip(*leaves))
        # draw the target point
        plt.scatter(target_point[0], target_point[1], color='black', marker='D')
        # re-draw the nearest neighbors found
        plt.scatter(*zip(*neighbors), color='red', marker='s')

        # draw circle from target point to furthest neighbor found
        radius = QuadNode.euclidean_distance(target_point, neighbors[-1])
        circle = plt.Circle((target_point[0], target_point[1]), radius, facecolor='none', edgecolor='#000000')
        plt.gca().add_patch(circle)

        # reset axis limits
        delta = 2
        plt.axis( [
            self.root.x - delta, self.root.x + self.root.width + delta, 
            self.root.y - delta, self.root.y + self.root.height + delta
            ] )

        plt.show()
