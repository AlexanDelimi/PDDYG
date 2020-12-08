from batch_insert import kdtree_batch
from serial_insert import kdtree_serial
from pprint import pprint


def squared_distance(point_1, point_2):
    
    total = 0
    dims = len(point_1)

    for i in range(dims):
        diff = abs(point_1[i] - point_2[i])
        total += diff**2

    return total


def closest_node(temp_node, best_node, target_point):
    
    if temp_node is None:
        return best_node

    if best_node is None:
        return temp_node

    dist_1 = squared_distance(temp_node.point, target_point)
    dist_2 = squared_distance(best_node.point, target_point)

    if (dist_1 < dist_2):
        return temp_node
    else:
        return best_node


def nearest_neighbor(root, target_point, dims, depth):

    if root is None:
        return None

    nextBranch = None
    otherBranch = None

    axis = depth % dims            # select axis based on depth
    # compare the property appropriate for the current depth
    if target_point[axis] < root.point[axis]:
        nextBranch = root.left_child
        otherBranch = root.right_child
    else:
        nextBranch = root.right_child
        otherBranch = root.left_child

    # recurse down the branch that's best according to the current depth
    temp_node = nearest_neighbor(nextBranch, target_point, dims, depth + 1)
    best_node = closest_node(temp_node, root, target_point)

    squared_radius = squared_distance(target_point, best_node.point)

    # We may need to check the other side of the tree. If the other side is closer than the radius,
    # then we must recurse to the other side as well. 'dist' is either a horizontal or a vertical line
    # that goes to an imaginary line that is splitting the plane by the root point.

    absolute_distance = target_point[axis] - root.point[axis]

    if squared_radius >= absolute_distance**2:
        temp_node = nearest_neighbor(otherBranch, target_point, dims, depth + 1)
        best_node = closest_node(temp_node, best_node, target_point)

    return best_node


def main():
    point_list = [(1,0), (0,1), (0,5), (0,6)]
    dims = len(point_list[0])

    ########## insert median ##########

    tree = kdtree_batch(point_list=point_list, dimensions=dims)
    pprint(tree.to_dict())  # the print order is a little bit crazy but okay

    nn = nearest_neighbor(tree, (0,2), dims, 0)
    print(nn.point)

    ########## insert serial ##########

    tree = kdtree_serial(None, point_list, dims)
    pprint(tree.to_dict())  # the print order is a little bit crazy but okay

    nn = nearest_neighbor(tree, (0,2), dims, 0)
    print(nn.point)


if __name__ == "__main__":
    main()
