# Summary

In this project, I wrote a program that will read the details for a graph from a file, allow a user to input a start and end destination and output the quickest route they can take to the city with the total time cost. We output the quickest route using
dijkstra's algorithm.

For lines 12-17, we add the vertices to the graph.
```Python
vertices = []
for line in input_vertices:
    city = line.strip()
    vertices.append(city)
    # Add vertex label to the graph
    g.addVertex(Vertex(city))
```
For lines 20-27, we add edges to the weighted graph.
```Python
edges = []
for line in input_edges:
    from_city, to_city, weight = line.strip().split(', ')
    from_index = vertices.index(from_city)
    to_index = vertices.index(to_city)
    weight = int(weight)
    
    g.addEdge(from_index, to_index, weight)
```

We use dijkstra's algorithm to find the shortest route for the start and destination city in lines 43-49:
```Python
for end in (nVerts - 1, nVerts - 2):
    # Grab the index numeric value and add it to the start value. Vice versa with the end value.
    start = vertices.index(start_city)
    end = vertices.index(destination_city)
    shortest = g.shortestPath(start, end) 
    cost = 0 if len(shortest) < 2 else sum(g.edgeWeight(shortest[i], shortest[i+1]) for i in range(len(shortest) - 1))
    path = ([(g.getVertex(v).name) for v in shortest])
```

Here is a sample run of the program which is similar in functionality to apple maps or google maps using the weighted graph data structure. 
```Jupyter Notebook
Cities: Seattle, San Francisco, Los Angeles, Denver, Kansas City, Chicago, Boston, New York, Atlanta, Miami, Dallas, Houston
Enter the start city:  San Francisco
Enter the destination city:  Boston
Shortest path from San Francisco to Boston is: San Francisco > Denver > Chicago > Boston
The total cost is: 3253
```
