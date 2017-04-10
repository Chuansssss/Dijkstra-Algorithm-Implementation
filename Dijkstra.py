# 4/10/2017 JcShang
# @USC EE555

import pandas as pd 
import sys
import re as re
import numpy as py

# read in the graph file
graph = open('Graph.dat', 'r')
# get the number of nodes
num_node = int(graph.readline())
# extract the lines in the .dat file
index = 0
lines= []
while (index != num_node):
	lines.append(graph.readline())
	index = index + 1

# the pattern for regular expression
pattern = ''
for i in range(1, num_node + 1):
	pattern += str(i) + '+' + '(.+)'
pa = re.compile(pattern)

# get the adjacency matrix
index = 0
result = py.zeros(shape = (num_node, num_node))

for i in lines:
	string = str(i)
	ma = pa.match(string)
	for x in range(0, num_node):
		result[index][x] = int(ma.group(x + 1))
	index += 1
# print result

# read in the input file
_input = open('Input.dat', 'r')
inPut = []

# extract the lines and put it in a matrix
while True:
	string = str(_input.readline())
	if string == str(0):
		break;
	inPut.append(string.split('\n')[0])
inPut = py.array(inPut)

# parse the matrix into sources and sinks
sources = []
sinks = []
length = len(inPut)
index = 0
while (index < length):
	if (index % 3 == 0):
		sources.append(inPut[index])
	if (index % 3 == 1):
		sinks.append(inPut[index])
	index += 1

sources = py.array(sources)
sinks = py.array(sinks)

num_pair = 0

#create the output.dat file if not existing
f = open('/Users/JcShang/Desktop/Output.dat', 'w+')

#start the Dijkstra's for each pair of source and sinik
while (num_pair != len(sources)):
	source = int(sources[num_pair]) - 1
	sink = int(sinks[num_pair]) - 1

	prev = py.zeros(shape = (num_node))
	visited = py.array([])
	visited = py.append(visited, [source], axis = 0)
	dis = py.zeros(shape = (num_node))

	while True:
		minDis = 999
		for i in visited:
			for j in range(0, num_node):
				#igore this node if already in the visited array since Dijkstra does not update previous nodes
				if j not in visited: 
					if dis[int(i)] + result[int(i)][int(j)] < minDis and result[int(i)][int(j)] > 0:
						minDis = dis[int(i)] + result[int(i)][int(j)]
						nextHop = j
						lastHop = i
		visited = py.append(visited, [nextHop], axis = 0)
		dis[nextHop] = dis[int(lastHop)] + result[int(lastHop)][nextHop]
		prev[nextHop] = lastHop
		if sink in visited:
			break

	#back track the shortest path from sink to source
	path = py.array([])
	path = py.append(path, [sink], axis = 0)
	while source not in path:
		path = py.append(path, [prev[int(path[-1])]], axis = 0)

	f.write(str(dis[sink]) + '\n') 

	#output the path in reverse order of the path array
	pointer = len(path) - 1
	while (pointer >= 0):
		f.write(str(path[-1] + 1) + '\n')
		path = path[:-1]
		pointer -= 1
	f.write('FFFF' + '\n')

	#algorithm finishes for the current pair of nodes
	num_pair += 1

#output the finishing tag in the output.dat file
f.write('0' + '\n')



