from pprint import pprint
from operator import itemgetter


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
                print('something went wrong 1')
        else:
            if self.right_child is None:
                self.right_child = TreeLeaf(point)
            elif is_leaf(self.right_child):
                self.right_child.point_list.append(point)
            elif not is_leaf(self.right_child):
                self.right_child.insert_leaf(point, dim)
            else:
                print('something went wrong 2')

    def to_dict(self):

        dictionary = {
            'value': self.value,
            'left child': None,
            'right child': None
        }

        if self.left_child != None:
            if is_leaf(self.left_child):
                dictionary['left child'] = self.left_child.point_list
            else:
                dictionary['left child'] = self.left_child.to_dict()

        if self.right_child != None:
            if is_leaf(self.right_child):
                dictionary['right child'] = self.right_child.point_list
            else:
                dictionary['right child'] = self.right_child.to_dict()

        return dictionary


def is_leaf(node):
    if type(node).__name__ == 'TreeLeaf':
        return True
    elif type(node).__name__ == 'TreeNode':
        return False

def sorted_array_to_bst(nums):
    '''nums must be a sorted list of unique values'''
    if not nums:
        return None
    mid_val = len(nums) // 2
    node = TreeNode(nums[mid_val])
    node.left_child = sorted_array_to_bst(nums[:mid_val])
    node.right_child = sorted_array_to_bst(nums[mid_val + 1:])
    return node


def main():
    lista = [(6,3), (2,6), (-2,4), (10,9), (3,1), (8,0), (8,10), (2,5), (12,-2)]
    
    list_x = sorted(list(set([point[0] for point in lista])))
    print(list_x)

    root = sorted_array_to_bst(list_x)
    # pprint(root.to_dict())

    root.insert_leaves(lista, 0)
    pprint(root.to_dict())


if __name__ == '__main__':
    main()