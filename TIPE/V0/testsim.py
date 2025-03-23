from encephalon import *
from axon import *
from pons import *
import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ser , port = test_serial()
run_sim(ANN([2,1,1]),port)

model = NN([2,1,1],ser)

model.W = {1: np.array([[ 1.0],[1.1]]), 2: np.array([[2]])}
model.b = {1: np.array([[0.]]), 2: np.array([[0.]])}

NN.set_weights_and_biases(model)

for _ in range(6):
    print(serial_read(ser,0.5))

points = []
sub = 6

for x in np.linspace(0, 5, sub):
    for y in np.linspace(0, 5, sub):
        z = model.use([x, y], 100)
        if z is None:
            print(f"No response for input: {[x, y]}")
            continue
        points.append([x, y, z[0]])

# for x in np.linspace(0, 5, sub):
#         z = model.use([x,0],5)
#         points.append([x,0,z[0]])

print(points)
points = np.array(points)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap="winter")