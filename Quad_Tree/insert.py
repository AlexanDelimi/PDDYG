import Classes

def insert(node, max_nodes_per_quad):
    cross_x = node.x
    cross_y = node.y
    PointsList = node.points
    NorthWestList = []
    NorthEastList = []
    SouthWestList = []
    SouthEastList = []
    for point in PointsList:
        if point[0] <= cross_x and point[1] >= cross_y:
            NorthWestList.append(point)

        elif cross_x <= point[0] and point[1] <= cross_y:
            SouthEastList.append(point)
        elif cross_x < point[0] and point[1] > cross_y:
            NorthEastList.append(point)
        elif point[0] < cross_x and point[1] < cross_y:
            SouthWestList.append(point)
    PointsList.clear()

    if len(NorthWestList) > 0: # Calculate coordinates for NorthWestChild
        NorthWestList.sort(key=lambda tup: tup[0])
        x_coor_nw = NorthWestList[0][0]
        NorthWestList.sort(key=lambda tup: tup[1])
        y_coor_nw = NorthWestList[-1][1]

        nwchild = Classes.Node((cross_x + x_coor_nw) / 2, (cross_y + y_coor_nw) / 2, None, None, None, None, NorthWestList) # Create TopLeftChild
        node.northwest = nwchild
        if len(NorthWestList) > max_nodes_per_quad: # Split the extra points
            insert(nwchild, max_nodes_per_quad)

    if len(NorthEastList) > 0: # Calculate coordinates for TopRightChild
        NorthEastList.sort(key=lambda tup: tup[0])
        x_coor_ne = NorthEastList[-1][0]
        NorthEastList.sort(key=lambda tup: tup[1])
        y_coor_ne = NorthEastList[-1][1]

        nechild = Classes.Node((cross_x + x_coor_ne) / 2, (cross_y + y_coor_ne) / 2, None, None, None, None, NorthEastList) # Create TopRightChild
        node.northeast = nechild
        if len(NorthEastList) > max_nodes_per_quad: # Split the extra points
            insert(nechild, max_nodes_per_quad)

    if len(SouthWestList) > 0: # Calculate coordinates for BottonLeftChild
        SouthWestList.sort(key=lambda tup: tup[0])
        x_coor_sw = SouthWestList[0][0]
        SouthWestList.sort(key=lambda tup: tup[1])
        y_coor_sw = SouthWestList[0][1]

        swchild = Classes.Node((cross_x + x_coor_sw) / 2, (cross_y + y_coor_sw) / 2, None, None, None, None, SouthWestList) # Create BottonLeftChild
        node.southwest = swchild
        if len(SouthWestList) > max_nodes_per_quad: # Split the extra points
            insert(swchild, max_nodes_per_quad)

    if len(SouthEastList) > 0: # Calculate coordinates for BottonRightChild
        SouthEastList.sort(key=lambda tup: tup[0])
        x_coor_se = SouthEastList[-1][0]
        SouthEastList.sort(key=lambda tup: tup[1])
        y_coor_se = SouthEastList[0][1]

        sechild = Classes.Node((cross_x + x_coor_se) / 2, (cross_y + y_coor_se) / 2, None, None, None, None, SouthEastList) # Create BottomRightChild
        node.southeast = sechild
        if len(SouthEastList) > max_nodes_per_quad: # Split the extra points
            insert(sechild, max_nodes_per_quad)