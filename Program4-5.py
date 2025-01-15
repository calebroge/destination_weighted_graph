# Caleb Roge and Thomas Bond
# Program4-5.py

from WeightedGraph import *

g = WeightedGraph()

input_vertices = open('Vertices.dat', mode='r')
input_edges = open('Edges.dat', mode='r')

# Add the vertices to the graph.
vertices = []
for line in input_vertices:
    city = line.strip()
    vertices.append(city)
    # Add vertex label to the graph
    g.addVertex(Vertex(city))

# Add the edges to the weighted graph.
edges = []
for line in input_edges:
    from_city, to_city, weight = line.strip().split(', ')
    from_index = vertices.index(from_city)
    to_index = vertices.index(to_city)
    weight = int(weight)
    
    g.addEdge(from_index, to_index, weight)

# This is to add the cities to an object together and display them to the user.
cities = []
for city in vertices:
    cities += [city]
print(f"Cities: {', '.join(cities)}")

# Grabs the number of vertices and adds them to the object.
nVerts = len(vertices)

# Inputs for the user to enter a start and destination city.
start_city = input('Enter the start city: ')
destination_city = input('Enter the destination city: ')

# For loop which uses shortest path algorithm (dijkstra's algorithm) to find the lowest cost to travel to the destination city from the start city.
for end in (nVerts - 1, nVerts - 2):
    # Grab the index numeric value and add it to the start value. Vice versa with the end value.
    start = vertices.index(start_city)
    end = vertices.index(destination_city)
    shortest = g.shortestPath(start, end) 
    cost = 0 if len(shortest) < 2 else sum(g.edgeWeight(shortest[i], shortest[i+1]) for i in range(len(shortest) - 1))
    path = ([(g.getVertex(v).name) for v in shortest])

# Prints out the path from the start city to the destination city. Also prints out the total cost which is calculated from the for loop.
print('Shortest path from', g.getVertex(start).name,
          'to', g.getVertex(end).name, 'is:',
         ' > '.join(path))
print(f'The total cost is: {cost}')