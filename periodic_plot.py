#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import sys



# Difference with respect to periodic boundaries
def periodic_diff(v1, v2, L):
	return ((v1 - v2 + L/2.) % L) - L/2.


# plot with respect to periodic boundaries
def periodic_plot(x1,y1,x2,y2,color, L):

	v1 = np.array((x1,y1))
	v2 = np.array((x2,y2))
	v2 = v1 + periodic_diff(v2, v1, L)
	x2,y2 = v2
	plt.plot([x1,x2], [y1,y2], c=color)

	return 


def plot_vertices(vertices, color):
	for x,y in vertices:
		plt.scatter(x,y,color=color)
	return 

def plot_edges(vertices, edges, color, L):
	for i1,i2 in edges:
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		periodic_plot(x1,y1,x2,y2,color, L)
	return	

def plot_hexagons(vertices, hexagons, color, L):
	
	for hexagon in hexagons:
		for i in range(0,5):
			i1 = hexagon[i]
			i2 = hexagon[i+1]
			x1,y1 = vertices[i1]
			x2,y2 = vertices[i2]
			periodic_plot(x1,y1,x2,y2,color,L)

		i1 = hexagon[-1]
		i2 = hexagon[0]
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		periodic_plot(x1,y1,x2,y2,color,L)
	return


# this would be really cool
def fill_hexagons(vertices, hexagons, L):
	pass



def save_plot(filename, L):


	# set axes
	plt.axis([0,L[0],0,L[1]])

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
# plot_edges(vertices, edges, "k", L)
plot_hexagons(vertices, hexagons, "k", L)

save_plot("periodic_lattice.jpg", L)


