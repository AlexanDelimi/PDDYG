import matplotlib.pyplot as plt
import matplotlib.patches as patches
from operator import itemgetter
from QuadNode import QuadNode

class QuadTree:
    '''
    Defines the tree by its root node
    using the points from the list of tuples provided
    and stores up to k points inside a leaf.
    '''
    def __init__(self, k, points):
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

    def k_nn(self, target_point, k):
        '''
        Get the k nearest neighbors around target
        among the points contained in the tree. 
        '''
        if k < 1:
            # invalid neighbors were asked
            return [target_point]
        else:
            nearest_list = []
            # search until k neighbors are found or all points are reported
            while (len(nearest_list) < k) and (len(nearest_list) < self.num_points):
                nn = self.root.nearest_neighbor(target_point, nearest_list)
                nearest_list.append(nn)
            return nearest_list

    def graph(self):
        '''
        Plot the tree.
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
        
        plt.show()

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
