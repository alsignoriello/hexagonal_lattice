#!/usr/bin/python
import numpy as np
import sys
from grid import generate_periodic_grid
from trace_periodic import trace_periodic_vertices

nx = int(sys.argv[1])
ny = int(sys.argv[2])

if nx % 2 != 0:
	print "Number of hexagons on x axis should be a multiple of 2"
	nx += 1

# side length of hexagon such that area = 1
s = (2)**(0.5) / (3 * (3)**0.5)**(0.5)

# width
w = 2. * s

# height
h = (3**(0.5) / 2.) * w


# generate grid
xx, yy, L = generate_periodic_grid(nx, ny, w, h)
np.savetxt("L", L)
# trace hexagons 
# return vertices and indices in counter clockwise order
vertices, indices = trace_periodic_vertices(nx,ny,xx,yy,w,h,L)

# write vertices
np.savetxt("vertices.txt", vertices)

# write edges
f = open("edges.txt", "w+")
for index in indices:
	for i in range(0,5):
		i1 = int(index[i])
		i2 = int(index[i+1])
		f.write("%d \t %d\n" % (i1,i2))
	i1 = int(index[-1])
	i2 = int(index[0])
	f.write("%d \t %d\n" % (i1,i2))
f.close()

# # write hexagons
np.savetxt("hexagons.txt", indices, delimiter="\t", fmt="%d")


