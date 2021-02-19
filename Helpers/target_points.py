'''
This file plots the inner and outter target points
to use as example image in report.
'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


inner_targets = [   (250,750), (750,750),
                    (250,250), (750,250)
                ]

outter_targets = [                  (500, 3000),
                    (-2000, 500),                 (3000, 500),
                                    (500, -2000)
                ]

# inner_targets = [   (166.6, 833.3), (500, 833.3), (833.3, 833.3),
#                     (166.6, 500),   (500, 500),   (833.3, 500),
#                     (166.6, 166,6), (500, 166.6), (833.3, 166.6)
#                 ]

# outter_targets = [  (-2000, 3000), (500, 3000), (3000, 3000),
#                     (-2000, 500),               (3000, 500),
#                     (-2000, -2000),(500, -2000),(3000, -2000)
#                 ]

fig,ax = plt.subplots()

plt.scatter(*zip(*inner_targets), label='inner targets')
plt.scatter(*zip(*outter_targets), label='outter targets')
ax.legend(bbox_to_anchor=(0.67, 0.85))

currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((0, 0), 1000, 1000, alpha=1, fill=False))

plt.show()