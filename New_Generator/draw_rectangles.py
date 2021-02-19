'''
This file contains functions that allow us to
draw new rectangles,
move them,
delete them
and store them.
Also it can redraw stored rectangles to edit them again.
'''

import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets  import RectangleSelector

from draggable_rectangle import DraggableRectangle, drs
from rectangles_csv_handling import drs_to_csv, csv_to_bars


def line_select_callback(eclick, erelease):
    global ax, drs
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata

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


def handle_close(event):
    global file, drs

    if len(drs) > 0:
        abspath = os.path.abspath(__file__)
        dirname = os.path.dirname(abspath)
        # save rectangles png at close event
        plt.savefig( os.path.join(dirname, 'Distributions', 'PNGs', file + '.png') )
        # save rectangles in drs to distribution csv file at close event
        drs_to_csv( os.path.join(dirname, 'Distributions', 'CSVs', file + '.csv'), drs)


def open_interface(filename, edit):
    global ax, drs, file
    
    file = filename
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    # connect listener for close event
    fig.canvas.mpl_connect('close_event', handle_close)

    # load rectangles to edit
    if edit == True:
        abspath = os.path.abspath(__file__)
        dirname = os.path.dirname(abspath)
        bars = csv_to_bars( os.path.join(dirname, 'Distributions', 'CSVs', file + '.csv') )
        drs = redraw_bars(bars, ax, drs)

    # prepare Rectangle Selector
    _ = RectangleSelector(ax, line_select_callback,
                        drawtype='box', useblit=False, button=[1], 
                        minspanx=5, minspany=5, spancoords='pixels', 
                        interactive=True)

    plt.show()
