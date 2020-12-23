from pprint import pprint


class TreeLeaf():
    def __init__(self, point):
        self.point_list = [point]


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.bst_y = None
    
    def insert_leaves(self, lista, dim):
        for point in lista:
            self.insert_leaf(point, dim)
    
    def insert_leaf(self, point, dim):
        if point[dim] <= self.value:
            if self.left_child is None:
                self.left_child = TreeLeaf(point)
            elif is_leaf(self.left_child):
                self.left_child.point_list.append(point)
            elif not is_leaf(self.left_child):
                self.left_child.insert_leaf(point, dim)
        else:
            if self.right_child is None:
                self.right_child = TreeLeaf(point)
            elif is_leaf(self.right_child):
                self.right_child.point_list.append(point)
            elif not is_leaf(self.right_child):
                self.right_child.insert_leaf(point, dim)

    def to_dict(self):

        dictionary = {
            'value': self.value,
            'left child': None,
            'right child': None,
            'bst y': None
        }

        if self.left_child is not None:
            if is_leaf(self.left_child):
                dictionary['left child'] = self.left_child.point_list
            else:
                dictionary['left child'] = self.left_child.to_dict()

        if self.right_child is not None:
            if is_leaf(self.right_child):
                dictionary['right child'] = self.right_child.point_list
            else:
                dictionary['right child'] = self.right_child.to_dict()

        if self.bst_y is not None:
            dictionary['bst y'] = self.bst_y.to_dict()

        return dictionary


def is_leaf(node):
    if type(node).__name__ == 'TreeLeaf':
        return True
    elif type(node).__name__ == 'TreeNode':
        return False

def build_1D_Range_Tree(nums):
    '''
    nums: sorted list of unique values
    '''
    if not nums:
        return None
    mid_val = len(nums) // 2
    node = TreeNode(nums[mid_val])
    node.left_child = build_1D_Range_Tree(nums[:mid_val])
    node.right_child = build_1D_Range_Tree(nums[mid_val + 1:])
    return node

def build_2D_Range_Tree(nums, lista):
    '''
    nums: sorted list of unique values

    lista: list of tuples with x coordinate in range [min(nums), max(nums)]
    '''
    if not nums:                      
        return None                       

    mid_val = len(nums) // 2             
    node = TreeNode(nums[mid_val])       

    left_lista = []             
    # No need to check for adequate length of left half of nums,
    # because it will always contain the last remaining element.
    for point in lista:
        # keep points in left half range 
        if nums[0] <= point[0] and point[0] <= nums[mid_val]:   
            left_lista.append(point)
    # same as 1D build
    node.left_child = build_2D_Range_Tree(nums[:mid_val], left_lista)   

    right_lista = []
    # We have to check for adequate length of right half of nums,
    # because it might not contain any elements.
    if mid_val+1 < len(nums):    
        for point in lista:
            # keep points in left half range
            if nums[mid_val+1] <= point[0] and point[0]<= nums[-1]:
                right_lista.append(point)
    # same as 1D build
    node.right_child = build_2D_Range_Tree(nums[mid_val + 1:], right_lista) 
    
    # Build the range tree of the second dimension
    # using the points passed down from the parent node.
    list_y = sorted(list(set([point[1] for point in lista])))        
    node.bst_y = build_1D_Range_Tree(list_y)                         
    node.bst_y.insert_leaves(lista, 1)                               

    return node


def main():
    # lista = [(6,3), (2,6), (-2,4), (10,9), (3,1), (8,0), (8,10), (2,5), (12,-2)]
    lista = [(1,2), (2,3), (3,1)]
    
    list_x = sorted(list(set([point[0] for point in lista])))
    root = build_2D_Range_Tree(list_x, lista)
    root.insert_leaves(lista, 0)

    pprint(root.to_dict())


if __name__ == '__main__':
    main()