#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import sys
from math import ceil


def plot_vertices(vertices, color):
	for x,y in vertices:
		plt.scatter(x,y,color=color)
	return 

def plot_edges(vertices, edges, color):
	for i1,i2 in edges:
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		plt.plot([x1,x2],[y1,y2],color=color)
	return	

def plot_hexagons(vertices, hexagons, color):
	
	for hexagon in hexagons:
		for i in range(0,5):
			i1 = hexagon[i]
			i2 = hexagon[i+1]
			x1,y1 = vertices[i1]
			x2,y2 = vertices[i2]
			plt.plot([x1,x2],[y1,y2],color=color)

		i1 = hexagon[-1]
		i2 = hexagon[0]
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		plt.plot([x1,x2],[y1,y2],color=color)
	return


# this would be really cool
def fill_hexagons(vertices, hexagons, L):
	pass



def save_plot(filename, L):


	# set axes
	plt.axis([-0.1, ceil(L[0])+0.1, -0.1, ceil(L[1])+0.1])

	# remove tick marks
	frame = plt.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])

	# save and close plot
	plt.savefig(filename)
	plt.close()




vertex_file = sys.argv[1]
edge_file = sys.argv[2]
hex_file = sys.argv[3]
L_file = sys.argv[4]

vertices = np.loadtxt(vertex_file)
edges = np.loadtxt(edge_file, dtype=int)
hexagons = np.loadtxt(hex_file, dtype=int)
L = np.loadtxt("L")
print L


plot_vertices(vertices, "c")
# plot_edges(vertices, edges, "k")
plot_hexagons(vertices, hexagons, "m")

save_plot("hex_lattice.jpg", L)


