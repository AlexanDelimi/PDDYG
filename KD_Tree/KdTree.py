from operator import itemgetter
from pprint import pprint
import matplotlib.pyplot as plt
from KdNode import KdNode
from math import sqrt


class KdTree():

    def __init__(self, point_list):
        self.num_points = len(point_list)
        self.xmin = min(point_list, key=itemgetter(0))[0]
        self.ymin = min(point_list, key=itemgetter(1))[1]
        self.xmax = max(point_list, key=itemgetter(0))[0]
        self.ymax = max(point_list, key=itemgetter(1))[1]
        self.root = KdTree.build_kdtree(point_list, 2)

    @staticmethod
    def build_kdtree(point_list, dimensions, depth: int = 0):
        
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
    
    def to_dict(self):
        return self.root.to_dict()
    
    def graph(self, delta=2):
        
        plt.figure()
        plt.axis( [self.xmin-delta, self.xmax+delta, self.ymin-delta, self.ymax+delta] )
        
        plt.grid(b=True, which='major', color='0.75', linestyle='--')
        plt.xticks([i for i in range(self.xmin-delta, self.xmax+delta, 1)])
        plt.yticks([i for i in range(self.ymin-delta, self.ymax+delta, 1)])
        
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

    def k_nn(self, target_point, k):
        if k < 1:
            return [target_point]
        else:
            nearest_list = []
            while (len(nearest_list) < k) and (len(nearest_list) < self.num_points):
                nn = KdNode.nearest_neighbor(self.root, target_point, 2, 0, nearest_list)
                nearest_list.append(nn.point)
            return nearest_list

    def graph_knn(self, target_point, neighbors, delta=2):

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
