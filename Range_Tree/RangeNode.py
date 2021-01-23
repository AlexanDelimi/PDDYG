class RangeLeaf():
    ''' Contains a list of points. '''

    def __init__(self, point):
        self.point_list = [point]


class RangeNode():
    ''' 
    Contains a value, left and right children
    and the corresponding range tree of the next dimension,
    if it has one.
    '''

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.bst_y = None
    
    def insert_leaves(self, lista, dim):
        ''' Begin insertion of leaves to node. '''

        for point in lista:
            self.insert_leaf(point, dim)
    
    def insert_leaf(self, point, dim):
        ''' Recursively insert leaf at correct branch. '''

        if point[dim] <= self.value:
            if self.left_child is None:
                self.left_child = RangeLeaf(point)
            elif RangeNode.is_leaf(self.left_child):
                self.left_child.point_list.append(point)
            elif not RangeNode.is_leaf(self.left_child):
                self.left_child.insert_leaf(point, dim)
        else:
            if self.right_child is None:
                self.right_child = RangeLeaf(point)
            elif RangeNode.is_leaf(self.right_child):
                self.right_child.point_list.append(point)
            elif not RangeNode.is_leaf(self.right_child):
                self.right_child.insert_leaf(point, dim)
    
    def insert_bst_y(self, lista):
        ''' Recursively create all range trees of second dimension. '''

        list_y = sorted(list(set([point[1] for point in lista])))
        self.bst_y = RangeNode.build_1D_Range_Tree(list_y)
        self.bst_y.insert_leaves(lista, 1)

        left_lista = []
        right_lista = []
        for point in lista:
            if point[0] <= self.value:
                left_lista.append(point)
            else:
                right_lista.append(point)
        
        if not ( RangeNode.is_leaf(self.left_child) or self.left_child is None ):
            self.left_child.insert_bst_y(left_lista)
        
        if not ( RangeNode.is_leaf(self.right_child) or self.right_child is None ):
            self.right_child.insert_bst_y(right_lista)

    def to_dict(self):
        ''' Return tree as dictionary to print. '''

        dictionary = {
            'value': self.value,
            'left child': None,
            'right child': None,
            'bst y': None
        }

        if self.left_child is not None:
            if RangeNode.is_leaf(self.left_child):
                dictionary['left child'] = self.left_child.point_list
            else:
                dictionary['left child'] = self.left_child.to_dict()

        if self.right_child is not None:
            if RangeNode.is_leaf(self.right_child):
                dictionary['right child'] = self.right_child.point_list
            else:
                dictionary['right child'] = self.right_child.to_dict()

        if self.bst_y is not None:
            dictionary['bst y'] = self.bst_y.to_dict()

        return dictionary

    @staticmethod
    def build_1D_Range_Tree(nums):
        '''
        Build the Range Tree of the first dimension
        using nums: a sorted list of unique values.
        '''
        if not nums:
            return None
        
        mid_val = len(nums) // 2
        node = RangeNode(nums[mid_val])
        node.left_child = RangeNode.build_1D_Range_Tree(nums[:mid_val])
        node.right_child = RangeNode.build_1D_Range_Tree(nums[mid_val + 1:])
        
        return node

    @staticmethod
    def is_leaf(node):
        ''' Return True if argument is leaf. '''
        
        if type(node).__name__ == 'RangeLeaf':
            return True
        elif type(node).__name__ == 'RangeNode':
            return False

    @staticmethod
    def squared_distance(point_1, point_2):
        ''' Return the euclidean distance of the points
            or infinity if either one is None. '''

        if point_1 is None or point_2 is None:
            return float('inf')

        total = 0
        dims = len(point_1)

        for i in range(dims):
            diff = point_1[i] - point_2[i]
            total += diff**2

        return total

    @staticmethod
    def closest_point(temp_best, best_point, target_point):
        ''' Return closest point to target
            between temp and best point. '''

        if temp_best is None:
            return best_point

        if best_point is None:
            return temp_best

        dist_1 = RangeNode.squared_distance(temp_best, target_point)
        dist_2 = RangeNode.squared_distance(best_point, target_point)

        if (dist_1 < dist_2):
            return temp_best
        else:
            return best_point

    @staticmethod
    def nearest_neighbor_x(root, target_point, nearest_list):
        ''' Get the point nearest to target
            according to the x dimension
            that is not already reported in nearest_list. '''
        
        if root is None:
            
            # nothing more to do here
            return None

        else:

            nextBranch = None
            otherBranch = None

            # compare the coordinate for the x axis
            if target_point[0] < root.value:
                nextBranch = root.left_child
                otherBranch = root.right_child
            else:
                nextBranch = root.right_child
                otherBranch = root.left_child

            if RangeNode.is_leaf(nextBranch):
                # search for best point in y bst
                best_point = RangeNode.nearest_neighbor_y(root.bst_y, target_point, nearest_list)
            else:
                # recurse down the best branch
                best_point = RangeNode.nearest_neighbor_x(nextBranch, target_point, nearest_list)

            squared_radius = RangeNode.squared_distance(target_point, best_point)
            absolute_distance = abs(target_point[0] - root.value)

            # check if the other branch is closer
            if squared_radius >= absolute_distance**2:
                
                temp_best = None
                if RangeNode.is_leaf(otherBranch):
                    # search for best point in y bst
                    temp_best = RangeNode.nearest_neighbor_y(root.bst_y, target_point, nearest_list)
                else:
                    # recurse down the other branch
                    temp_best = RangeNode.nearest_neighbor_x(otherBranch, target_point, nearest_list)
                
                best_point = RangeNode.closest_point(temp_best, best_point, target_point)

            return best_point

    @staticmethod
    def nearest_neighbor_y(root, target_point, nearest_list):
        ''' Get the point nearest to target
            according to the y dimension
            that is not already reported in nearest_list. '''
        
        if root is None:
            
            # nothing more to do here
            return None

        elif RangeNode.is_leaf(root):
            
            # get unreported point in leaf (if there is one) closest to target 
            best_point = None
            min_distance = float('inf')
            for point in root.point_list:
                if point not in nearest_list:
                    dist = RangeNode.squared_distance(point, target_point)
                    if dist < min_distance:
                        min_distance = dist
                        best_point = point

            return best_point

        else:   # root is internal node

            nextBranch = None
            otherBranch = None

            # compare the coordinate for the y axis
            if target_point[1] < root.value:
                nextBranch = root.left_child
                otherBranch = root.right_child
            else:
                nextBranch = root.right_child
                otherBranch = root.left_child

            # recurse down the best branch
            best_point = RangeNode.nearest_neighbor_y(nextBranch, target_point, nearest_list)

            squared_radius = RangeNode.squared_distance(target_point, best_point)
            absolute_distance = abs(target_point[1] - root.value)

            # check if the other branch is closer
            if squared_radius >= absolute_distance**2:
                temp_best = RangeNode.nearest_neighbor_y(otherBranch, target_point, nearest_list)
                best_point = RangeNode.closest_point(temp_best, best_point, target_point)

            return best_point

    @staticmethod
    def get_leaves(node, leaflist):
        '''
        Recursively report all leaves.
        '''
        # a deepest node is found
        if RangeNode.is_leaf(node):
            # report leaves
            leaflist += node.point_list
        
        # the node has more children
        else:
            # continue the search for each child of the node
            if node.left_child is not None:
                leaflist = RangeNode.get_leaves(node.left_child, leaflist)
            if node.right_child is not None:
                leaflist = RangeNode.get_leaves(node.right_child, leaflist)
        
        return leaflist
