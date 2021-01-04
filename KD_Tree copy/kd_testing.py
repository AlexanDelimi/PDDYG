from KdTree import KdTree
from pprint import pprint


def main1():
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    ktree = KdTree(point_list)
    pprint(ktree.to_dict())
    ktree.graph()


def main2():
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]

    ktree = KdTree(point_list)

    target_point = (2,4)
    knn = ktree.k_nn(target_point, k=4)

    ktree.graph_knn(target_point, knn)

if __name__ == "__main__":
    main2()
