'''
https://matplotlib.org/users/event_handling.html#draggable-rectangle-exercise
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
        # print(self.id)
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
        # print(event)
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, _ = self.rect.contains(event)     # '_' was 'attrd' for some reason
        if not contains: return
        # print('event contains', self.rect.xy)

        if event.button == 3:
            x0, y0 = self.rect.xy
            self.press = x0, y0, event.xdata, event.ydata
        elif event.button == 2:
            for i, d_rect in enumerate(drs):
                if d_rect.id == self.id:
                    d_rect.rect.set_visible(False)
                    del drs[i]
                    # print(str(d_rect.id) + ' deleted')
                # else:
                    # print(d_rect.id)
    
        self.rect.figure.canvas.draw()


    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
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
