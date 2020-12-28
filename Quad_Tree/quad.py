from random import uniform

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Node:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.children = {}

    def contains(self, points):
        pts = []
        for point in points:
            if self.x <= point[0] < self.x + self.width and self.y <= point[1] < self.y + self.height:
                pts.append(point)
        return pts

    def subdivide(self, k, points):
        if len(points) <= k:
            self.children = points
            return

        w_ = float(self.width / 2)
        h_ = float(self.height / 2)

        self.children['southwest'] = Node(self.x, self.y, w_, h_)
        p = self.children['southwest'].contains(points)
        self.children['southwest'].subdivide(k, p)

        self.children['southeast'] = Node(self.x+w_, self.y, w_, h_)
        p = self.children['southeast'].contains(points)
        self.children['southeast'].subdivide(k, p)

        self.children['northwest'] = Node(self.x, self.y+h_, w_, h_)
        p = self.children['northwest'].contains(points)
        self.children['northwest'].subdivide(k, p)

        self.children['northeast'] = Node(self.x+w_, self.y+h_, w_, h_)
        p = self.children['northeast'].contains(points)
        self.children['northeast'].subdivide(k, p)

    def find_children(self, nodelist, leaflist):
        if self.children.__class__.__name__ == "list":
            nodelist.append(self)
            leaflist += self.children
        elif self.children.__class__.__name__ == "dict":
            for child in self.children:
                nodelist = self.children[child].find_children(nodelist, leaflist)
        return nodelist, leaflist

class QTree:
    def __init__(self, k, xmin, ymin, width, height):  # k ο μέγιστος αριθμός σημείων σε κάθε κουτί
        self.threshold = k
        self.root = Node(xmin-0.01, ymin-0.01, width+0.02, height+0.02)

    def add_points(self, points):
        self.root.subdivide(self.threshold, points)

    def graph(self):
        fig = plt.figure(figsize=(15, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        children, leaves = self.root.find_children([], [])
        for node in children:
            ax.add_patch(patches.Rectangle((node.x, node.y), node.width, node.height, fill=False))
        plt.scatter(*zip(*leaves))
        plt.show()
        return





   #def height(self, lista):
   #    first_and_second = sorted(points, key=lambda tup: (tup[0], tup[1]))
   #    first_x = first_and_second[0][0]
   #    last_x = first_and_second[-1][0]
   #    height = abs(first_x) + abs(last_x)
   #    return height
   #
   #def width(self, lista):
   #    first_and_second = sorted(points, key=lambda tup: (tup[0], tup[1]))
   #    first_y = first_and_second[0][1]
   #    last_y = first_and_second[-1][1]
   #    width = abs(first_y) + abs(last_y)
   #    return width






data = [(-3, 1), (-5, 3), (-2, 4), (0, 0), (1, 1), (4, 1), (2, 3)]

#points=  [Point(data.__getitem__(x)[0], data.__getitem__(x)[1]) for x in range(len(data))]
# height_width(points)
qtree = QTree(6, points)
#qtree.subdivide()
#qtree.graph(qtree.root)

def main():
    points = [(uniform(0, 100), uniform(0, 100)) for _ in range(10)]
