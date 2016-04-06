#!/usr/bin/python
import numpy as np
import sys
from numpy import random


# shift vertices randomly
# s is side length of hexagon
def shift_vertices(vertices, s):
	for i,(x,y) in enumerate(vertices):
		x += random.uniform(-s/2.,s/2.)
		y += random.uniform(-s/2.,s/2.)
		vertices[i,0] = x
		vertices[i,1] = y
	return vertices




file = sys.argv[1]

vertices = np.loadtxt(file)

# side length of hexagon such that area = 1
s = (2)**(0.5) / (3 * (3)**0.5)**(0.5)
vertices = shift_vertices(vertices, s)

np.savetxt("noise_vertices.txt", vertices)