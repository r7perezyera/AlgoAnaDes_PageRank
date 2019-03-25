# Encoding: UTF-8
# Author: Roberto Téllez Perezyera A01374866

import sys
it = iter(sys.stdin.read().splitlines())

# crea lista donde todos los elementos son la tupla sin el ")"
# el ultimo elemento es el numero de iteraciones
lin = next(it).split(" ")

iters = int(lin[0])
print("iters:",iters)

lin.pop(0)

graph = []

for tupla in lin:
    values = tupla.strip("()")
    pairLst = [int(x) for x in values.split(",")]
    graph.append(pairLst)
print("graph:",graph)

# lists containing exclusively outlinks and inlinks
outlinks = []
inlinks = []
for pair in graph:
    outlinks.append(pair[0])
    inlinks.append(pair[1])
print("outlinks",outlinks)
print("inlinks",inlinks)

# get total number of nodes
outMax = max(outlinks)
inMax = max(inlinks)
maxes = [outMax, inMax]
numNodes = max(maxes)
print("total nodes:",numNodes)

# list of nodes
nodes = list(range(1, numNodes + 1, 1))
print("nodes list:",nodes)

# list of starting rank per nodes
startingPR = 1/numNodes
pageRankPrev = [startingPR for i in range(len(nodes))]
print("pageRankPrev:",pageRankPrev)

pageRank = [0] * numNodes
print("pageRank",pageRank)

howManyOutlinks = []
for j in range(numNodes):
    outCount = 0
    for elem in graph:
        if elem[0] == j + 1:
            outCount += 1
    howManyOutlinks.append(outCount)

# nodes pointing at node of current page
pointingNodes = []
for j in range(numNodes):
    lst = []
    for elem in graph:
        if elem[1] == j + 1:
            lst.append(elem[0])
    pointingNodes.append(lst)
print("Quienes le apuntan al nodo Pi:",pointingNodes)

for k in range(iters):
    for i in range(numNodes):
        sum = 0
        for elem in pointingNodes[i]:
            sum += pageRankPrev[elem - 1] / howManyOutlinks[elem - 1]
        pageRank[i-1] = sum

    pageRankPrev = pageRank.copy()

print(pageRankPrev)
