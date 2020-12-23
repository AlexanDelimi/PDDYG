import insert
import Classes
import rebalance
def boundaries(points): # Calculate rectangle's boundaries
    points.sort(key=lambda tup: tup[0])
    mid_x = (points[0][0] + points[-1][0]) / 2 # Lowest and highest point's x axis
    print('hellll0oooo')
    print(mid_x)
    points.sort(key=lambda tup: tup[1])
    mid_y = (points[0][1] + points[-1][1]) / 2 # Lowest and highest point's y axis
    return mid_x, mid_y


def build(points, max_nodes_per_quad):
    mid_x, mid_y = boundaries(points) # Calculate first cross boundaries
    root = Classes.Node(mid_x, mid_y, None, None, None, None, points)
    insert.insert(root, max_nodes_per_quad)
    return root
