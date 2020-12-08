class Node():

    def __init__(self, point, left_child, right_child):
        self.point = point
        self.left_child = left_child
        self.right_child = right_child

    def to_dict(self):
        
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