from math import sqrt


class QuadNode:
    '''
    A node defines a rectangle and 
    stores either four children or up to k leaves.
    '''
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.children = {}

    def contains(self, points):
        '''
        Return all points from an original list
        that are inside the bounds of the node's rectangle.
        '''
        pts = []
        for point in points:
            if self.x <= point[0] < self.x + self.width and self.y <= point[1] < self.y + self.height:
                pts.append(point)
        return pts

    def subdivide(self, k, points):
        '''
        Recursively divide a node and pass the appropriate  points down to its children
        until the maximum capacity k is not exceeded.
        '''
        # store leaves if they don't exceed maximum capacity
        if len(points) <= k:
            self.children = points
            return

        # new rectangles dimension
        w_ = float(self.width / 2)
        h_ = float(self.height / 2)

        self.children['sw'] = QuadNode(self.x, self.y, w_, h_)          # create sw child
        p = self.children['sw'].contains(points)                    # select associated points
        self.children['sw'].subdivide(k, p)                         # recurse down again

        self.children['se'] = QuadNode(self.x+w_, self.y, w_, h_)       # create se child
        p = self.children['se'].contains(points)                    # select associated points
        self.children['se'].subdivide(k, p)                         # recurse down again

        self.children['nw'] = QuadNode(self.x, self.y+h_, w_, h_)       # create nw child
        p = self.children['nw'].contains(points)                    # select associated points
        self.children['nw'].subdivide(k, p)                         # recurse down again

        self.children['ne'] = QuadNode(self.x+w_, self.y+h_, w_, h_)    # create ne child
        p = self.children['ne'].contains(points)                    # select associated points
        self.children['ne'].subdivide(k, p)

    def find_children(self, nodelist, leaflist):
        '''
        Recursively report for the deepest nodes and their leaves.
        '''
        # a deepest node is found
        if self.children.__class__.__name__ == "list":
            # report the node and its leaves
            nodelist.append(self)
            leaflist += self.children
        # the node has more children
        elif self.children.__class__.__name__ == "dict":
            # continue the search for each child of the node
            for child in self.children:
                nodelist, leaflist = self.children[child].find_children(nodelist, leaflist)
        return nodelist, leaflist
    
    @staticmethod
    def euclidean_distance(point_1, point_2):
        ''' 
        Return the euclidean distance of the points
        or infinity if either one of them is None. 
        '''
        if point_1 is None or point_2 is None:
            return float('inf')

        total = 0
        dims = len(point_1)

        for i in range(dims):
            diff = point_1[i] - point_2[i]
            total += diff**2

        return sqrt(total)

    @staticmethod
    def closest_point(temp_best, best_point, target_point):
        ''' 
        Return closest point to target
        between temp and best point. 
        '''
        if temp_best is None:
            return best_point

        if best_point is None:
            return temp_best

        dist_1 = QuadNode.euclidean_distance(temp_best, target_point)
        dist_2 = QuadNode.euclidean_distance(best_point, target_point)

        if (dist_1 < dist_2):
            return temp_best
        else:
            return best_point
    
    def get_distances(self, target_point, from_direction):
        '''
        Return the distances between the target point
        and the brothers of the node according to the direction of the node.
        '''
        distances = {}

        if from_direction == 'nw':
            distances['ne'] = abs(target_point[0] - (self.x + self.width))
            distances['sw'] = abs(target_point[1] - self.y)
            distances['se'] = QuadNode.euclidean_distance(target_point, (self.x + self.width, self.y))

        elif from_direction == 'ne':
            distances['nw'] = abs(target_point[0] - self.x)
            distances['se'] = abs(target_point[1] - self.y)
            distances['sw'] = QuadNode.euclidean_distance(target_point, (self.x, self.y))

        elif from_direction == 'sw':
            distances['se'] = abs(target_point[0] - (self.x + self.width))
            distances['nw'] = abs(target_point[1] - (self.y + self.height))
            distances['ne'] = QuadNode.euclidean_distance(target_point, (self.x + self.width, self.y + self.height))

        elif from_direction == 'se':
            distances['sw'] = abs(target_point[0] - self.x)
            distances['ne'] = abs(target_point[1] - (self.y + self.height))
            distances['nw'] = QuadNode.euclidean_distance(target_point, (self.x, self.y + self.height))

        return distances

    def nearest_neighbor(self, target_point, nearest_list):
        '''
        Recursively report the one nearest node to the target point
        that is not already reported in the nearest list.
        '''
        if self.children.__class__.__name__ == "list":
            
            # return child closest to target
            best_point = None
            min_distance = float('inf')
            for leaf in self.children:
                if leaf not in nearest_list:
                    dist = QuadNode.euclidean_distance(leaf, target_point)
                    if dist < min_distance:
                        min_distance = dist
                        best_point = leaf
            
            return best_point
        
        elif self.children.__class__.__name__ == "dict":
            
            # get child that contains target and store the other children
            nextChildDir = ''
            otherChildren = {}

            if target_point[1] >= self.y + self.height/2:
                nextChildDir += 'n'
            else:
                nextChildDir += 's'

            if target_point[0] >= self.x + self.width/2:
                nextChildDir += 'e'
            else:
                nextChildDir += 'w'

            for direction, node in self.children.items():
                if direction == nextChildDir:
                    nextChildNode = node
                else:
                    otherChildren[direction] = node
            
            # recurse down the best branch
            best_point = nextChildNode.nearest_neighbor(target_point, nearest_list)

            # best distance from target
            squared_radius = QuadNode.euclidean_distance(target_point, best_point)

            # get distances = { direction : distance } from brothers 
            distances = nextChildNode.get_distances(target_point, nextChildDir)
            

            # call nearest_neighbor for each promising brother to get temp_best
            for direction, distance in distances.items():
                if squared_radius >= distance:
                    temp_best = self.children[direction].nearest_neighbor(target_point, nearest_list)
                    # compare current temp_best with current best_point and store to best_point 
                    best_point = QuadNode.closest_point(temp_best, best_point, target_point)
            
            return best_point
