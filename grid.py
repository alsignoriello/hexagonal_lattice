#!/usr/bin/python
import numpy as np

# hexagonal grid should be spaced as such:
# 0.5 height on y axis
# 0.25 width on x axis
# The final length of the grid should be a scale of:
# 1.5 width 
# 1 height	
# http://www.redblobgames.com/grids/hexagons/	

# currently this works for periodic boundaries
# may modify for normal boundaries
def generate_grid(nx, ny, w, h):

	# length of box on x axis
	lx = (nx / 2.) * 1.5 * w

	# length of box on y axis
	ly = ny * h 

	# generate grid of coordinates
	xs = np.linspace(0., lx, 3 * nx + 1)
	xs = xs[:-1] # periodic boundary condition

	ys = np.linspace(0., ly, 2 * ny + 1)
	ys = ys[:-1]  # periodic boundary condition

	xx, yy = np.meshgrid(xs, ys)

	L = np.array((lx,ly))

	return xx, yy, L
