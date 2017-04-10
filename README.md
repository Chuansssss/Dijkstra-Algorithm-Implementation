# Dijkstra-Algorithm-Implementation
This is a mini program that implements the Dijkstra algorithm on non-negative graphs, both directed and undirected, to find the shortest path between any two nodes.
# Format of Graph, Input and Output
## Graph.dat
The structure of the graph is described ini the Graph.dat file. In this file you need to specify the following:
a. Number of Vertices
b. A weighted graph representedn in the form of 'adjacent list'
c. For each vertex, you need to keep a list of their weights (weights range from 0 to 9 for simplicity). Aweight of 0 means there is no edge between the two vertices.
## Input.dat
The pair of nodes you want to calculate are listed in this file. In this file you need to specify the following:
a. Multiple sets of 'source and destination' vertices
b. use FF to indicate the end of a set of source and destination pair and a 0 to represent the end of all input sets
## Output.dat
The shortest distance and the path are listed for each pair of nodes. For each set of input,
a. Write out the weighted path length followed by
b. Vertices of the entire 'shortest path' from source to destination
c. If there are multiple paths with the same weighted shortest path length choose the one with the minimum number of hops
d. Use FFFF to indicate the end of a set of input and 0 to represent the end of all inputs.

## Example of Graph.dat, Input.dat and Output.dat
Graph.dat format
6
102235415060
122033425060
152330435165
112233405160
102031415062
102035405260
The first row indicate the number of vertices (nodes)
The second row indicates the following distances from node 1
~ The distance between node 1 and itself is 0
~ The distance between node 1 and node 2 is 10
~ The distance between node 1 and node 3 is 0 (i.e. no direct link)
~ The distance between node 1 and node 4 is 5
~ The distance between node 1 and node 5 is 10 0 (i.e. no direct link)
And so on.

Input.dat format
1
3
FF
1
4
FF
1
5
FF
1
6
FF
2
6
FF
3
6
FF
0
The pairs of nodes that are to be calculated are (1, 3), (1, 4), (1,5), (1, 6), (2, 6) and (3, 6).

Output.dat format
3.0
1.0
4.0
5.0
3.0
FFFF
1.0
1.0
4.0
FFFF
2.0
1.0
4.0
5.0
FFFF
4.0
1.0
4.0
5.0
6.0
FFFF
5.0
2.0
4.0
5.0
6.0
FFFF
3.0
3.0
5.0
6.0
FFFF
0
The above means that the shortest distance between 1 and 3 is 3 and the path is 1-4-5-3.
And so on.
