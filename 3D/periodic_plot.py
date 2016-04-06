#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import sys
from mpl_toolkits.mplot3d import Axes3D


# Difference with respect to periodic boundaries
def periodic_diff(v1, v2, L):
	return ((v1 - v2 + L/2.) % L) - L/2.


# plot with respect to periodic boundaries
def periodic_plot(x1,y1,x2,y2,z1,z2,color, L):

	v1 = np.array((x1,y1))
	v2 = np.array((x2,y2))
	v2 = v1 + periodic_diff(v2, v1, L)
	x2,y2 = v2
	ax.plot([x1,x2], [y1,y2], [z1,z2], c=color)

	return 


def plot_vertices(vertices, color, z):
	for x,y in vertices:
		ax.scatter(x,y,z,color=color)
	return 

def plot_edges(vertices, z1, z2, color, L):

	for x,y in vertices:
		periodic_plot(x,y,x,y,z1,z2,color, L)
	return	

def plot_hexagons(vertices, hexagons, z, color, L):
		
	z1 = z
	z2 = z

	for hexagon in hexagons:
		for i in range(0,5):
			i1 = hexagon[i]
			i2 = hexagon[i+1]
			x1,y1 = vertices[i1]
			x2,y2 = vertices[i2]
			periodic_plot(x1,y1,x2,y2,z1,z2,color,L)

		i1 = hexagon[-1]
		i2 = hexagon[0]
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		periodic_plot(x1,y1,x2,y2,z1,z2,color,L)
	return


# this would be really cool
def fill_hexagons(vertices, hexagons, L):
	pass



def save_plot(filename, L):


	# set axes
	ax.axis([0,L[0],0,L[1]])

	# remove tick marks
	frame = ax.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])

	# save and close plot
	ax.savefig(filename)
	ax.close()




vertex_file = sys.argv[1]
edge_file = sys.argv[2]
hex_file = sys.argv[3]
L_file = sys.argv[4]

vertices = np.loadtxt(vertex_file)
edges = np.loadtxt(edge_file, dtype=int)
hexagons = np.loadtxt(hex_file, dtype=int)
L = np.loadtxt("L")
print L


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z1 = 0
plot_vertices(vertices, "c", z1)
# plot_edges(vertices, edges, "k", L)
plot_hexagons(vertices, hexagons, z1, "m", L)

z2 = 1
plot_vertices(vertices, "c", z2)
plot_hexagons(vertices, hexagons, z2, "m", L)


# plot edges between them
plot_edges(vertices, z1, z2, "m", L)


plt.show()
# save_plot("periodic_lattice.jpg", L)


