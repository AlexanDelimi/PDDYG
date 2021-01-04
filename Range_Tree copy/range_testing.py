from pprint import pprint
from RangeTree import RangeTree


def main1():
    lista = [(6,3), (2,6), (-2,4), (10,9), (3,1), (8,0), (8,10), (2,5), (12,-2), (3,5)]
    # lista = [(1,2), (2,3), (2,4), (3,1)]
    
    rtree = RangeTree(lista)

    pprint(rtree.to_dict())

    rtree.graph()


def main2():
    lista = [(6,3), (2,6), (-2,4), (10,9), (3,1), (8,0), (8,10), (2,5), (12,-2), (3,5)]
    # lista = [(1,2), (2,3), (5,4), (3,1),(5,7),(0,0)]

    # build 2D range tree
    rtree = RangeTree(lista)

    rtree.graph()

    # perform knn query around target
    target_point = (2,5)
    knn = rtree.k_nn(target_point, k=7)

    rtree.graph_knn(target_point, knn)
    


if __name__ == '__main__':
    main2()