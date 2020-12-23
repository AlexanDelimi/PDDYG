import functions
import gatherTreeNodes
import knnSearch

list = []
path = []


def search(node,point):
    if node is None:
        return False

    if functions.isLeaf(node) is True:
        if point in node.points:
                return True
        return False
    else:
        return search(functions.relChild(point,node),point)



def stypidQ(root,k,point): #na rotisoume
    gatherTreeNodes.gather_tree_nodes(root)
    qList = gatherTreeNodes.general_list
    kList = []
    for qpoint in qList:
        if len(kList < k -1):
            kList.append([point, knnSearch.euclideanDistance(qpoint,point)])
        else:
            kList.sort(key=lambda x: x[1])
            dist = knnSearch.euclideanDistance(qpoint,point)
            if dist < kList(k-1)[1]:
                kList.pop()
                kList.append(qpoint)




