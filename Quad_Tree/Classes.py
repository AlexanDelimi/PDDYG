import build
import insert
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, x, y,  northwest, northeast, southeast, southwest, points):
        self.x = x
        self.y = y
        self.northwest = northwest
        self.northeast = northeast
        self.southeast = southeast
        self.southwest = southwest
        self.points = points
        #self.children = []
        points.sort(key=lambda tup: tup[0])
        self.width = (points[0][0] + points[-1][0])
        points.sort(key=lambda tup: tup[1])
        self.height = (points[0][1] + points[-1][1])

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_points(self):
        return self.points

class QuadTree:
    def __init__(self, k, lists):  # k ο μέγιστος αριθμός σημείων σε κάθε κουτί και n είναι ο αριθμός των σημείων
        self.threshold = k
        self.points = lists
        self.root = Node(0, 0, None, None, None, None, self.points)

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_points(self):
        return self.points

    def build(self):
        mid_x=self.root.width/2
        mid_y = self.root.height/2  # Calculate first cross boundaries
        insert.insert(self.root, self.threshold)

    def graph(self):
        fig = plt.figure(figsize=(15, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        c = find_children(self.root)
        print("Number of segments: %d" %len(c))
        "Number of segments: %d" % len(c)
        areas = set()
        for el in c:
            areas.add(el.x * el.y)
        print("Minimum segment area: %.3f units" %min(areas))
        "Minimum segment area: %.3f units" % min(areas)
        for n in c:
            ax.add_patch(patches.Rectangle((n.x, n.y), n.width, n.height, fill=False))
        x = [point[0] for point in self.root.points]
        y = [point[1] for point in self.root.points]
        plt.plot(x, y, 'ro')
        plt.show()
        return


def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children
