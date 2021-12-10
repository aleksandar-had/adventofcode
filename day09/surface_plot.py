import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = range(100)
y = range(100)

with open("input.txt", 'r') as f:
    heatmap = np.array([[int(h) for h in line] for line in f.read().splitlines()])
    
plt.figure(num=1,figsize=(10,10))

hf = plt.figure(num=1)
ha = hf.add_subplot(111, projection='3d')

X, Y = np.meshgrid(range(100),range(100))
ha.plot_surface(X, Y, heatmap)

plt.show()