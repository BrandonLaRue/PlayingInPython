import matplotlib.pyplot as plt
from numpy import *


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot([1, 2, 3, 1], [1, 4, 2, 1], [1, 5, 9, 1], 'ro-')
plt.pause(0.1)
ax.plot([45], [6], [26], 'bo')
plt.show()


