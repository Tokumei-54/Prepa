#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:51:39 2020

@author: laurent
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter # création du .gif

plt.clf()

xmin, xmax = -15, +15
n = 2 * 150 + 1 # nombre de points
dt = 0.02 # pas temporel
dx = (xmax - xmin)/(n - 1) # pas spatial
c = 1.8 # vitesse de propagation

x = np.linspace(xmin, xmax, n)

Ei = np.exp(-x** 2) # champ électrique initial
Bi = np.zeros(n) # champ magnétique initial

def nextEB():
    global E, B
    B[1:n-1] = B[1:n-1] - dt*(E[2:n] - E[0:n-2])/2/dx
    E[1:n-1] = E[1:n-1] - c**2*dt*(B[2:n] - B[0:n-2])/2/dx
    
def init():
    global E, B
    E = Ei.copy()
    B = Bi.copy()
    return line1, line2

def animate(i):
    nextEB()
    line1.set_data(x, E)
    line2.set_data(x, B)
    return line1, line2

fig = plt.figure(1)
ax = plt.axes(xlim = (-10, 10), ylim = (-0.5, 1.1))
line1, = ax.plot(x, Ei, lw=1.5, color='r', label='champ électrique')
line2, = ax.plot(x, Bi, lw=1.5, color='b', label='champ magnétique')
# plt.plot(x, Ei, 'r--', lw=1)
# plt.plot(x, Bi, 'b--', lw=1)

# animate : nom de la fonction permettant de tracer chaque image sucessivement à l’aide du paramètre i.
# frames: nombre d'images constituant l'animation
# repeat_delay: The delay in milliseconds between consecutive animation runs, if repeat is True.
# interval : intervalle de temps séparant deux images successives en milliseconde
# blit : seuls les éléments de l’image modifiés seront redessinées à chaque image si blit est égal à True
# repeat : l’animation ne s’exécutera qu’une fois, ne se repètera pas si repeat est égal à False.
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 330,
       repeat_delay = 5000, interval = 150, blit = False, repeat = True)
plt.grid() 
plt.legend(loc = 'lower right', fontsize = 12)
plt.xlabel("abscise selon la direction de propagation [unité arbitraire]", fontsize=12)
plt.ylabel("champ électromagnétique [unité arbitraire]", fontsize=12)
plt.title("Propagation du champ sous la forme de deux OPP", fontsize=14)

plt.show()

# sauvegarder l'animation au format .gif, lisible par Firefox
anim.save('Propagation.gif', writer=PillowWriter(fps=10)) # fps = Movie frame rate per second