#!/usr/bin/bash


nx=$1
ny=$2

echo "Number of hexagons in x direction = "$nx
echo "Number of hexagons in y direction = "$ny


# # periodic boundary condtions
python periodic_hex_lattice.py $nx $ny
# python noise.py "vertices.txt" 

python periodic_plot.py vertices.txt edges.txt hexagons.txt L

# # # normal boundaries
# python hex_lattice.py $nx $ny 
# python plot.py vertices.txt edges.txt hexagons.txt L