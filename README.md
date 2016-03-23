# Hexagonal Lattice

Generates a hexagonal flat-topped lattice. 

It can be simulated such that there are no boundary conditions or there are periodic boundary conditions. 


# Running the simulation

|Parameter| Definition| Range |
|---------|-----------|-------|
| nx | number of hexagons in x direction | even positive int |
| ny | number of hexagons in y direction | positive int |



sh run.sh [nx] [ny]

vertices.txt (x,y) coordinates for every vertex in the lattice

edges.txt (index1, index2) indices for every edge between two vertices in the lattice

hexagons.txt (index0, index1, ... indexN) indices in counter-clockwise order that form every hexagon in the lattice


# Requirements

numpy (1.8.1)

matplotlib (1.3.1)