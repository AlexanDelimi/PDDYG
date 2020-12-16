'''
https://stackoverflow.com/questions/12052379/matplotlib-draw-a-selection-area-in-the-shape-of-a-rectangle-with-the-mouse
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets  import RectangleSelector
from draggable_rectangle_1 import DraggableRectangle, drs


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




fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
# fig, ax = plt.subplots()

rs = RectangleSelector(ax, line_select_callback,
                       drawtype='box', useblit=False, button=[1], 
                       minspanx=5, minspany=5, spancoords='pixels', 
                       interactive=True)

plt.show()

print('okay')
