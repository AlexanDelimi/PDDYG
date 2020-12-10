import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, x0, y0, w, h, points):
        self.x0 = x0
        self.y0 = y0
        self.width = w
        self.height = h
        self.points = points
        self.children = []

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_points(self):
        return self.points


class QTree:
    def __init__(self, k, lista):  # k ο μέγιστος αριθμός σημείων σε κάθε κουτί και n είναι ο αριθμός των σημείων
        self.threshold = k
        self.points = []
        self.addManyPoints(lista)
        self.root = Node(0, 0, self.width(lista), self.height(lista), points)

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def addManyPoints(self, lista):
        for point in lista:
            self.add_point(point[0], point[1])

    def get_points(self):
        return self.points

    def subdivide(self):
        recursive_subdivide(self.root, self.threshold)

    def graph(self):
        fig = plt.figure(figsize=(12, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        c = find_children(self.root)
        print()
        "Number of segments: %d" % len(c)
        areas = set()
        for el in c:
            areas.add(el.width * el.height)
        print()
        "Minimum segment area: %.3f units" % min(areas)
        for n in c:
            ax.add_patch(patches.Rectangle((n.x0, n.y0), n.width, n.height, fill=False))
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        plt.plot(x, y, 'ro')
        plt.show()
        return

    def height(self, lista):
        first_and_second = sorted(points, key=lambda tup: (tup[0], tup[1]))
        first_x = first_and_second[0][0]
        last_x = first_and_second[-1][0]
        height = abs(first_x) + abs(last_x)
        return height

    def width(self, lista):
        first_and_second = sorted(points, key=lambda tup: (tup[0], tup[1]))
        first_y = first_and_second[0][1]
        last_y = first_and_second[-1][1]
        width = abs(first_y) + abs(last_y)
        return width


def recursive_subdivide(node, k):
    if len(node.points) <= k:
        return

    w_ = float(node.width / 2)
    h_ = float(node.height / 2)

    p = contains(node.x0, node.y0, w_, h_, node.points)
    x1 = Node(node.x0, node.y0, w_, h_, p)
    recursive_subdivide(x1, k)

    p = contains(node.x0, node.y0 + h_, w_, h_, node.points)
    x2 = Node(node.x0, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x2, k)

    p = contains(node.x0 + w_, node.y0, w_, h_, node.points)
    x3 = Node(node.x0 + w_, node.y0, w_, h_, p)
    recursive_subdivide(x3, k)

    p = contains(node.x0 + w_, node.y0 + h_, w_, h_, node.points)
    x4 = Node(node.x0 + w_, node.y0 + h_, w_, h_, p)
    recursive_subdivide(x4, k)

    node.children = [x1, x2, x3, x4]


def contains(x, y, w, h, points):
    pts = []
    for point in points:
        if point[0] < x or point[0] > x + w or point[1] < y or point[1] > y + h:
            continue
        pts.append(point)
    return pts


def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children


points = [(-3, 1), (-5, 3), (-2, 4), (0, 0), (1, 1), (4, 1), (2, 3)]

# height_width(points)
qtree = QTree(3, points)
qtree.subdivide()
qtree.graph()
print(qtree.height(points))
print(qtree.width(points))
