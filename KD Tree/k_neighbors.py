from neighbor import nearest_neighbor
from batch_insert import kdtree_batch
from pprint import pprint


def k_nn(root, target_point, dims, num_points, k):
    nearest_list = []
    while (len(nearest_list) < k) and (len(nearest_list) < num_points):
        nn = nearest_neighbor(root, target_point, dims, 0, nearest_list)
        nearest_list.append(nn.point)
    return nearest_list

def main():
    point_list = [(1,0), (0,1), (1,1), (0,6), (2,3)]
    dims = len(point_list[0])

    tree = kdtree_batch(point_list=point_list, dimensions=dims)
    pprint(tree.to_dict())

    knn = k_nn(tree, (0,0), dims, num_points=len(point_list), k=3)
    print(knn)


if __name__ == "__main__":
    main()

