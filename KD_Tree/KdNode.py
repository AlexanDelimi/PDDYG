import matplotlib.pyplot as plt

line_width = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.3]


class KdNode():
    ''' Contains the point, the right and the left child. '''

    def __init__(self, point, left_child, right_child):
        self.point = point
        self.left_child = left_child
        self.right_child = right_child

    def to_dict(self):
        ''' Return tree as dictionary to print. '''
        
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

    def plot_tree(self, min_x, max_x, min_y, max_y, prev_node, branch, dimensions, depth=0):
        ''' Plot the Kd Tree. '''

        # tree          (sub)tree to be plotted
        # prev_node     parent node
        # branch        True if (sub)tree is left child of parent node, 
        #               False if (sub)tree is right child of parent node
    
        cur_node = self.point
        left_branch = self.left_child
        right_branch = self.right_child
    
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
            left_branch.plot_tree(min_x, max_x, min_y, max_y, cur_node, True, dimensions, depth+1)
    
        if right_branch is not None:
            right_branch.plot_tree(min_x, max_x, min_y, max_y, cur_node, False, dimensions, depth+1)

    @staticmethod
    def squared_distance(point_1, point_2):
        ''' Return the squared distance of the points. '''
        
        total = 0
        dims = len(point_1)

        for i in range(dims):
            diff = point_1[i] - point_2[i]
            total += diff**2

        return total

    @staticmethod
    def closest_node(temp_node, best_node, target_point):
        ''' Return the closest node to target
        between temp and best nodes. '''
        
        if temp_node is None:
            return best_node

        if best_node is None:
            return temp_node

        dist_1 = KdNode.squared_distance(temp_node.point, target_point)
        dist_2 = KdNode.squared_distance(best_node.point, target_point)

        if (dist_1 < dist_2):
            return temp_node
        else:
            return best_node

    @staticmethod
    def nearest_neighbor(node, target_point, dims, depth, nearest_list):
        ''' Return the nearest neighbor to target point
        that is not in nearest_list of reported neighbors. '''

        if node is None:
            return None

        if node.point in nearest_list:  # skip node if already found
            
            nearest_left = KdNode.nearest_neighbor(node.left_child, target_point, dims, depth + 1, nearest_list)
            nearest_right = KdNode.nearest_neighbor(node.right_child, target_point, dims, depth + 1, nearest_list)
            
            return KdNode.closest_node(nearest_left, nearest_right, target_point)
        
        else:

            nextBranch = None
            otherBranch = None

            axis = depth % dims            # select axis based on depth
            # compare the property appropriate for the current depth
            if target_point[axis] < node.point[axis]:
                nextBranch = node.left_child
                otherBranch = node.right_child
            else:
                nextBranch = node.right_child
                otherBranch = node.left_child

            # recurse down the branch that's best according to the current depth
            temp_node = KdNode.nearest_neighbor(nextBranch, target_point, dims, depth + 1, nearest_list)
            best_node = KdNode.closest_node(temp_node, node, target_point)

            squared_radius = KdNode.squared_distance(target_point, best_node.point)

            # We may need to check the other side of the tree. If the other side is closer than the radius,
            # then we must recurse to the other side as well. 'dist' is either a horizontal or a vertical line
            # that goes to an imaginary line that is splitting the plane by the root point.

            absolute_distance = target_point[axis] - node.point[axis]

            if squared_radius >= absolute_distance**2:
                temp_node = KdNode.nearest_neighbor(otherBranch, target_point, dims, depth + 1, nearest_list)
                best_node = KdNode.closest_node(temp_node, best_node, target_point)

            return best_node
    
    def get_points(self, pointlist):
        '''
        Recursively report all the nodes.
        '''
        # check if the original root is None (empty tree)
        if self is None:
            return pointlist
        
        pointlist.append(self.point)
        if self.left_child is not None:
            pointlist = self.left_child.get_points(pointlist)
        if self.right_child is not None:
            pointlist = self.right_child.get_points(pointlist) 
        
        return pointlist