from quad import QTree
from random import uniform
from math import sqrt
import matplotlib.pyplot as plt


def euclidean_distance(point_1, point_2):
    ''' Return the euclidean distance of the points
        or infinity if either one is None. '''

    if point_1 is None or point_2 is None:
        return float('inf')

    total = 0
    dims = len(point_1)

    for i in range(dims):
        diff = point_1[i] - point_2[i]
        total += diff**2

    return sqrt(total)


def closest_point(temp_best, best_point, target_point):
    ''' Return closest point to target
        between temp and best point. '''

    if temp_best is None:
        return best_point

    if best_point is None:
        return temp_best

    dist_1 = euclidean_distance(temp_best, target_point)
    dist_2 = euclidean_distance(best_point, target_point)

    if (dist_1 < dist_2):
        return temp_best
    else:
        return best_point


def get_distances(target_point, nextChildNode, nextChildDir):
    
    distances = {}

    if nextChildDir == 'nw':
        distances['ne'] = abs(target_point[0] - (nextChildNode.x + nextChildNode.width))
        distances['sw'] = abs(target_point[1] - nextChildNode.y)
        distances['se'] = euclidean_distance(target_point, (nextChildNode.x + nextChildNode.width, nextChildNode.y))

    elif nextChildDir == 'ne':
        distances['nw'] = abs(target_point[0] - nextChildNode.x)
        distances['se'] = abs(target_point[1] - nextChildNode.y)
        distances['sw'] = euclidean_distance(target_point, (nextChildNode.x, nextChildNode.y))

    elif nextChildDir == 'sw':
        distances['se'] = abs(target_point[0] - (nextChildNode.x + nextChildNode.width))
        distances['nw'] = abs(target_point[1] - (nextChildNode.y + nextChildNode.height))
        distances['ne'] = euclidean_distance(target_point, (nextChildNode.x + nextChildNode.width, nextChildNode.y + nextChildNode.height))

    elif nextChildDir == 'se':
        distances['sw'] = abs(target_point[0] - nextChildNode.x)
        distances['ne'] = abs(target_point[1] - (nextChildNode.y + nextChildNode.height))
        distances['nw'] = euclidean_distance(target_point, (nextChildNode.x, nextChildNode.y + nextChildNode.height))

    return distances

def nearest_neighbor(root, target_point, nearest_list):

    if root.children.__class__.__name__ == "list":
        
        # return child closest to target
        best_point = None
        min_distance = float('inf')
        for leaf in root.children:
            if leaf not in nearest_list:
                dist = euclidean_distance(leaf, target_point)
                if dist < min_distance:
                    min_distance = dist
                    best_point = leaf
        
        return best_point
    
    elif root.children.__class__.__name__ == "dict":
        
        # get child that contains target and store the other children
        nextChildDir = ''
        otherChildren = {}

        if target_point[1] >= root.y + root.height/2:
            nextChildDir += 'n'
        else:
            nextChildDir += 's'

        if target_point[0] >= root.x + root.width/2:
            nextChildDir += 'e'
        else:
            nextChildDir += 'w'

        for direction, node in root.children.items():
            if direction == nextChildDir:
                nextChildNode = node
            else:
                otherChildren[direction] = node
        
        # recurse down the best branch
        best_point = nearest_neighbor(nextChildNode, target_point, nearest_list)

        # best distance from target
        squared_radius = euclidean_distance(target_point, best_point)

        # get distances = { direction : distance } from brothers 
        distances = get_distances(target_point, nextChildNode, nextChildDir)
        

        # call nearest_neighbor for each promising brother to get temp_best
        for direction, distance in distances.items():
            if squared_radius >= distance:
                temp_best = nearest_neighbor(root.children[direction], target_point, nearest_list)
                # compare current temp_best with current best_point and store to best_point 
                best_point = closest_point(temp_best, best_point, target_point)
        
        return best_point


def k_nn(root, target_point, num_points, k):
    ''' Get the k nearest neighbors around target
        among of total of num_points contained in root tree. '''
    
    if k < 1:
        return [target_point]
    else:
        nearest_list = []
        while (len(nearest_list) < k) and (len(nearest_list) < num_points):
            nn = nearest_neighbor(root, target_point, nearest_list)
            nearest_list.append(nn)
        return nearest_list


def draw_circle(target_point, furthest_point):
    radius = euclidean_distance(target_point, furthest_point)
    circle = plt.Circle((target_point[0], target_point[1]), radius, facecolor='none', edgecolor='#000000')
    plt.gca().add_patch(circle)


def main():

    # points = [ (-1,-1), (-1,1), (1,-1), (1,1) ]
    # points = [
    #     (6,3), (2,6), (-2,4), (7,6), (3,1), (8,0),
    #     (8,10), (2,5), (12,-2), (3,5), (-1,8), (0,5),
    #     (3,8), (0,2), (-1,0), (10,2), (11,0)
    #     ] 
    points = [(uniform(0, 100), uniform(0, 100)) for _ in range(10000)]
    qtree=QTree(3, points)
    qtree.graph()

    target_point = (uniform(0, 10000), uniform(0, 10000)) #(0.5,0.5) #(8.2,1.7) #(10,7) #(1,0) #(4.9,4.1)
    
    plt.scatter(target_point[0], target_point[1], color='black', marker='D')

    knn = k_nn(qtree.root, target_point, len(points), 10000)

    plt.scatter(*zip(*knn), color='red', marker='s')
    draw_circle(target_point, knn[-1])

    # reset axis limits
    delta = 2
    plt.axis( [qtree.root.x-delta, qtree.root.x+qtree.root.width+delta, qtree.root.y-delta, qtree.root.y+qtree.root.height+delta] )
    
    plt.show()


if __name__=='__main__':
    main()