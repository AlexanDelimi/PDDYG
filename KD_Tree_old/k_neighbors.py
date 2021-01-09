from neighbor import nearest_neighbor, squared_distance
from batch_insert import kdtree_batch
from pprint import pprint
from draw_kd_tree import plot_figure
from operator import itemgetter
import matplotlib.pyplot as plt
from math import sqrt


def k_nn(root, target_point, dims, num_points, k):
    if k < 1:
        return [target_point]
    else:
        nearest_list = []
        while (len(nearest_list) < k) and (len(nearest_list) < num_points):
            nn = nearest_neighbor(root, target_point, dims, 0, nearest_list)
            nearest_list.append(nn.point)
        return nearest_list

def draw_point(target_point):
    plt.plot(target_point[0], target_point[1], marker='o', color='#ff007f')
    circle = plt.Circle((target_point[0], target_point[1]), 0.3, facecolor='#ff007f', edgecolor='#ff007f', alpha=0.5)
    plt.gca().add_patch(circle)

def draw_circle(target_point, furthest_nn):
    radius = sqrt(squared_distance(target_point, furthest_nn))
    circle = plt.Circle((target_point[0], target_point[1]), radius, facecolor='#ffd83d', edgecolor='#ffd83d', alpha=0.5)
    plt.gca().add_patch(circle)

def draw_neighbors(knn):
    for point in knn:
        plt.plot(point[0], point[1], 'go')
        circle = plt.Circle((point[0], point[1]), 0.3, facecolor='#33cc00', edgecolor='#33cc00', alpha=0.5)
        plt.gca().add_patch(circle)


def main():
    point_list = [(1,0), (0,1), (1,1), (0,6), (2,3)]
    dims = len(point_list[0])

    min_val = min(min(point_list, key=itemgetter(0))[0],min(point_list, key=itemgetter(1))[1])
    max_val = max(max(point_list, key=itemgetter(0))[0],max(point_list, key=itemgetter(1))[1])
    delta = 2

    tree = kdtree_batch(point_list=point_list, dimensions=dims)
    pprint(tree.to_dict())

    plot_figure(tree, dims, min_val, max_val, delta, 1)

    target_point = (2,4)
    knn = k_nn(tree, target_point, dims, num_points=len(point_list), k=2)
    print(knn)

    draw_point(target_point)
    draw_circle(target_point, knn[-1])
    draw_neighbors(knn)

    plt.show()


if __name__ == "__main__":
    main()

