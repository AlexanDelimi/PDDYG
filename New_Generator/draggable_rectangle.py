'''
This files contains the class that allows us to move and delete rectangles.
'''

import numpy as np
import matplotlib.pyplot as plt

ID = 0
drs = []

class DraggableRectangle:

    def __init__(self, rect):
        global ID
        self.rect = rect
        self.press = None
        self.id = ID
        ID = ID + 1

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        global drs
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, _ = self.rect.contains(event)
        if not contains: return

        if event.button == 3:
            x0, y0 = self.rect.xy
            self.press = x0, y0, event.xdata, event.ydata
        elif event.button == 2:
            for i, d_rect in enumerate(drs):
                if d_rect.id == self.id:
                    d_rect.rect.set_visible(False)
                    del drs[i]
    
        self.rect.figure.canvas.draw()


    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        self.rect.figure.canvas.draw()


    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
