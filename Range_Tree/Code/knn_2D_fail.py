from pprint import pprint
from build_2D_Range_Tree import build_2D_Range_Tree, is_leaf
import matplotlib.pyplot as plt
from math import sqrt
from operator import itemgetter


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


def closest_point(temp_best, best_point, target_point):
    ''' Return closest point to target
        between temp and best point. '''

    if temp_best is None:
        return best_point

    if best_point is None:
        return temp_best

    dist_1 = squared_distance(temp_best, target_point)
    dist_2 = squared_distance(best_point, target_point)

    if (dist_1 < dist_2):
        return temp_best
    else:
        return best_point


def nearest_neighbor_x(root, target_point, axis, nearest_list):
    ''' Get the point nearest to target
        according to the axis dimension
        that is not already reported in nearest_list. '''
    
    if root is None:
        
        # nothing more to do here
        return None

    else:

        nextBranch = None
        otherBranch = None

        # compare the coordinate for the given axis
        if target_point[axis] < root.value:
            nextBranch = root.left_child
            otherBranch = root.right_child
        else:
            nextBranch = root.right_child
            otherBranch = root.left_child

        if is_leaf(nextBranch):
            # search for best point in y bst
            best_point = nearest_neighbor_y(root.bst_y, target_point, 1, nearest_list)
        else:
            # recurse down the best branch
            best_point = nearest_neighbor_x(nextBranch, target_point, axis, nearest_list)

        squared_radius = squared_distance(target_point, best_point)
        absolute_distance = abs(target_point[axis] - root.value)

        # check if the other branch is closer
        if squared_radius >= absolute_distance**2:
            
            temp_best = None
            if is_leaf(otherBranch):
                # search for best point in y bst
                temp_best = nearest_neighbor_y(root.bst_y, target_point, 1, nearest_list)
            else:
                # recurse down the other branch
                temp_best = nearest_neighbor_x(otherBranch, target_point, axis, nearest_list)
            
            best_point = closest_point(temp_best, best_point, target_point)

        return best_point


def nearest_neighbor_y(root, target_point, axis, nearest_list):
    ''' Get the point nearest to target
        according to the axis dimension
        that is not already reported in nearest_list. '''
    
    if root is None:
        
        # nothing more to do here
        return None

    elif is_leaf(root):
        
        # get unreported point in leaf (if there is one) closest to target 
        best_point = None
        min_distance = float('inf')
        for point in root.point_list:
            if point not in nearest_list:
                dist = squared_distance(point, target_point)
                if dist < min_distance:
                    min_distance = dist
                    best_point = point

        return best_point

    else:   # root is internal node

        nextBranch = None
        otherBranch = None

        # compare the coordinate for the given axis
        if target_point[axis] < root.value:
            nextBranch = root.left_child
            otherBranch = root.right_child
        else:
            nextBranch = root.right_child
            otherBranch = root.left_child

        # recurse down the best branch
        best_point = nearest_neighbor_y(nextBranch, target_point, axis, nearest_list)

        squared_radius = squared_distance(target_point, best_point)
        absolute_distance = abs(target_point[axis] - root.value)

        # check if the other branch is closer
        if squared_radius >= absolute_distance**2:
            temp_best = nearest_neighbor_y(otherBranch, target_point, axis, nearest_list)
            best_point = closest_point(temp_best, best_point, target_point)

        return best_point


def draw_circle(target_point, furthest_point):
    radius = sqrt(squared_distance(target_point, furthest_point))
    circle = plt.Circle((target_point[0], target_point[1]), radius, facecolor='none', edgecolor='#000000')
    plt.gca().add_patch(circle)

def k_nn(root, target_point, num_points, k):
    ''' Get the k nearest neighbors around target
        among of total of num_points contained in root tree. '''
    
    if k < 1:
        return [target_point]
    else:
        nearest_list = []
        while (len(nearest_list) < k) and (len(nearest_list) < num_points):
            nn = nearest_neighbor_x(root, target_point, 0, nearest_list)
            nearest_list.append(nn)
            print(nearest_list)
        return nearest_list

def main():
    lista = [(6,3), (2,6), (-2,4), (10,9), (3,1), (8,0), (8,10), (2,5), (12,-2), (3,5)]
    # lista = [(1,2), (2,3), (5,4), (3,1),(5,7),(0,0)]

    # plot points
    plt.scatter(*zip(*lista))

    # build 2D range tree
    list_x = sorted(list(set([point[0] for point in lista])))
    root = build_2D_Range_Tree(list_x, lista)
    root.insert_leaves(lista, 0)

    # pprint(root.to_dict())

    # perform knn query around target
    target_point = (4.5,5)
    knn = k_nn(root, target_point, num_points=len(lista), k=5)
    
    # draw target, neighbors and enclosing circle
    plt.scatter(target_point[0], target_point[1], color='black', marker='D')
    plt.scatter(*zip(*knn), color='red', marker='s')
    draw_circle(target_point, knn[-1])

    # reset axis limits
    min_val = min(min(lista, key=itemgetter(0))[0],min(lista, key=itemgetter(1))[1])
    max_val = max(max(lista, key=itemgetter(0))[0],max(lista, key=itemgetter(1))[1])
    delta = 2
    plt.axis( [min_val-delta, max_val+delta, min_val-delta, max_val+delta] )

    # show final plot
    plt.show()

if __name__ == '__main__':
    main()