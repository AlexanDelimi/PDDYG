from QuadTree import QuadTree
from random import uniform

def main1():

    points = [(uniform(0, 100), uniform(0, 100)) for _ in range(100)]
    qtree=QuadTree(3, points)
    qtree.graph()

def main2():
    
    # points = [ (-1,-1), (-1,1), (1,-1), (1,1) ]
    # points = [
    #     (6,3), (2,6), (-2,4), (7,6), (3,1), (8,0),
    #     (8,10), (2,5), (12,-2), (3,5), (-1,8), (0,5),
    #     (3,8), (0,2), (-1,0), (10,2), (11,0)
    #     ] 
    points = [(uniform(0, 100), uniform(0, 100)) for _ in range(100)]
    qtree = QuadTree(5, points)

    qtree.graph()

    target_point = (uniform(0, 100), uniform(0, 100)) #(0.5,0.5) #(8.2,1.7) #(10,7) #(1,0) #(4.9,4.1)

    knn = qtree.k_nn(target_point, 10)

    qtree.graph_knn(target_point, knn)

if __name__=='__main__':
    main2()