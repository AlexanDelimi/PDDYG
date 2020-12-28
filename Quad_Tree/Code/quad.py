from operator import itemgetter
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
                nodelist, leaflist = self.children[child].find_children(nodelist, leaflist)
        return nodelist, leaflist


class QTree:
    def __init__(self, k, points):  # k ο μέγιστος αριθμός σημείων σε κάθε κουτί
        self.threshold = k
        xmin = min(points, key=itemgetter(0))[0]
        ymin = min(points, key=itemgetter(1))[1]
        xmax = max(points, key=itemgetter(0))[0]
        ymax = max(points, key=itemgetter(1))[1]
        width = xmax - xmin
        height = ymax - ymin
        self.root = Node(xmin - 0.01, ymin - 0.01, width + 0.02, height + 0.02)
        self.root.subdivide(self.threshold, points)

    def graph(self):
        fig = plt.figure(figsize=(15, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        children, leaves = self.root.find_children([], [])
        print(len(leaves))
        for node in children:
            ax.add_patch(patches.Rectangle((node.x, node.y), node.width, node.height, fill=False))
        plt.scatter(*zip(*leaves))
        plt.show()
        return


def main():
    points = [(uniform(0, 100), uniform(0, 100)) for _ in range(100)]
    qtree=QTree(3, points)
    qtree.graph()

if __name__=='__main__':
    main()
