#!/usr/bin/python
import numpy as np 

def periodic_indices(index, length):
	if index == -1:
		return length - 1
	if index == length:
		return 0
	return index



def pos_in_list(vertices, x, y):

	for j,v in enumerate(vertices):
		if v[0] == x and v[1] == y:
			return j
		if v[0] == -1 and v[1] == -1:
			vertices[j][0] = x
			vertices[j][1] = y
			return j
	return -1


# trace hexagon vertices -- counter-clockwise
# starting from ix, iy
# add vertices to list if they aren't there already
def trace_hexagon(xx, yy, vertices, ix, iy, L):
	
	# counter-clockwise indices for vertices in hexagon
	indices = np.zeros(6)

	# necessary for periodic bounary condition
	len_x = len(xx[0,:])
	len_y = len(yy[:,0])

	# counter-clockwise order
	# Index 0 = left corner index 
	vx = xx[iy,ix]
	vy = yy[iy,ix]
	pos = pos_in_list(vertices, vx, vy)
	indices[0] = pos

	# Index 1 = right 1, down 1
	ix_1 = periodic_indices(ix + 1, len_x)
	iy_1 = periodic_indices(iy - 1, len_y)
	vx = xx[iy_1,ix_1]
	vy = yy[iy_1,ix_1]
	pos = pos_in_list(vertices, vx,vy)
	indices[1] = pos

	# Index 2 = right 2
	ix_2 = periodic_indices(ix_1 + 2, len_x)
	iy_2 = periodic_indices(iy_1, len_y)
	vx = xx[iy_2, ix_2]
	vy = yy[iy_2, ix_2]
	pos = pos_in_list(vertices, vx, vy)
	indices[2] = pos

	# Index 3 = up 1, right 1
	ix_3 = periodic_indices(ix_2 + 1, len_x)
	iy_3 = periodic_indices(iy_2 + 1, len_y)
	vx = xx[iy_3, ix_3]
	vy = yy[iy_3, ix_3]
	pos = pos_in_list(vertices, vx, vy)
	indices[3] = pos

	# Index 4 = up 1, left 1
	ix_4 = periodic_indices(ix_3 - 1, len_x)
	iy_4 = periodic_indices(iy_3 + 1, len_y)
	vx = xx[iy_4, ix_4]
	vy = yy[iy_4, ix_4]
	pos = pos_in_list(vertices, vx, vy)
	indices[4] = pos

	# Index 5 = left 2
	ix_5 = periodic_indices(ix_4 - 2, len_x)
	iy_5 = periodic_indices(iy_4, len_y)
	vx = xx[iy_5, ix_5]
	vy = yy[iy_5, ix_5]
	pos = pos_in_list(vertices, vx, vy)
	indices[5] = pos

	# Index 6 == Index 0 = left 1, down 1
	ix_6 = periodic_indices(ix_5 - 1, len_x)
	iy_6 = periodic_indices(iy_5 - 1, len_y)
	vx = xx[iy_6, ix_6]
	vy = yy[iy_6, ix_6]
	if ix_6 != ix and iy_6 != iy:
		print "Did not cycle back to vertex"

	return indices


def trace_periodic_vertices(nx, ny, xx, yy, w, h, L):
	n_hex = nx * ny
	print "There are %d hexagons" % n_hex

	# indices in counter-clockwise order
	hex_indices = np.zeros((n_hex, 6))

	# each vertex has 3 polygons attached
	n_vertices = (6 * n_hex) / 3

	# list of x,y vertices
	vertices = np.zeros((n_vertices, 2))
	vertices.fill(-1)

	# left corner indices
	x_left_0 = []
	x_left_1 = []
	for i in range(0,len(xx[0,:]),3):
		if i % 2 == 0:
			x_left_1.append(i)
		if i % 2 != 0:
			x_left_0.append(i)

	# keep track of vertices and indices
	curr_v = 0 # current vertex
	hex_counter = 0
	for i in range(0, 2 * ny):
		iy = i
		if i % 2 == 0:
			for j in x_left_0:
				ix = j
				indices = trace_hexagon(xx, yy, vertices, ix, iy, L)
				hex_indices[hex_counter, :] = indices 
				hex_counter += 1
		else:
			for j in x_left_1:
				ix = j
				indices = trace_hexagon(xx, yy, vertices, ix, iy, L)
				hex_indices[hex_counter, :] = indices 
				hex_counter += 1				

	return vertices, hex_indices

