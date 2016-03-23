#!/usr/bin/python
import numpy as np



# shift vertices randomly
# s is side length of hexagon
def shift_vertices(vertices, s):
	for i,(x,y) in enumerate(vertices):
		x += random.uniform(-s/2.,s/2.)
		y += random.uniform(-s/2.,s/2.)
		vertices[i,0] = x
		vertices[i,1] = y
	return vertices
