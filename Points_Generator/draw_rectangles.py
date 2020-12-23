'''
https://stackoverflow.com/questions/12052379/matplotlib-draw-a-selection-area-in-the-shape-of-a-rectangle-with-the-mouse
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets  import RectangleSelector

from draggable_rectangle import DraggableRectangle, drs
from rectangles_csv_handling import drs_to_csv, csv_to_bars


def line_select_callback(eclick, erelease):
    global ax, drs
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata

    # rect = plt.Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2) )
    # ax.add_patch(rect)

    rect = ax.bar(x=min(x1,x2)+abs(x1-x2)/2, height=abs(y1-y2), width=abs(x1-x2), bottom=min(y1,y2), color='b')[0]
    dr = DraggableRectangle(rect)
    dr.connect()
    drs.append(dr)


def redraw_bars(bars, ax, drs):
    for bar in bars:
        rect = ax.bar(bar['x'], bar['height'], bar['width'], bar['bottom'], color='b')[0]
        dr = DraggableRectangle(rect)
        dr.connect()
        drs.append(dr)
    return drs


if __name__ == '__main__':
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 2 lines bellow only when redrawing
    bars = csv_to_bars('rect_test.csv')
    drs = redraw_bars(bars, ax, drs)

    rs = RectangleSelector(ax, line_select_callback,
                        drawtype='box', useblit=False, button=[1], 
                        minspanx=5, minspany=5, spancoords='pixels', 
                        interactive=True)

    plt.show()

    drs_to_csv('rect_test.csv', drs)
    # drs_to_csv('rect_test_npoints.csv', drs)