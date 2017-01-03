import numpy as np 
from math import sqrt


# Euclidean distance between (x,y) coordinates
def euclidean_distance(x0, y0, x1, y1):
	return sqrt((x0 - x1)**2 + (y0 - y1)**2)

# Area of a polygon
def area(vertices):
	n = len(vertices)
	cross_product = 0
	for i in range(0,n):
		x0,y0 = vertices[i,:]
		if i == n - 1:
			x1,y1 = vertices[0,:]
		else:
			x1,y1 = vertices[i+1,:]
		cross_product += ((x0 * y1) - (x1 * y0))
	return 0.5 * abs(cross_product)


# Perimeter of a polygon
def perimeter(vertices):
	n = len(vertices)
	perimeter = 0.
	for i in range(0,n):
		x0,y0 = vertices[i]
		if i == n - 1:
			x1,y1 = vertices[0]
		if i != n - 1:
			x1,y1 = vertices[i+1]
		dist = euclidean_distance(x0, y0, x1, y1)
		perimeter += dist
	return perimeter



vertices = np.loadtxt("vertices.txt")
hexagons = np.loadtxt("hexagons.txt").astype(int)


for hexagon in hexagons:
	v = np.zeros((6,2))
	for i in range(0, len(hexagon)):
		x,y = vertices[hexagon[i],:]
		v[i,0] = x 
		v[i,1] = y

	a = area(v)
	p = perimeter(v)
	print a,p