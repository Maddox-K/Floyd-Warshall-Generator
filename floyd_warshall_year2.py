import numpy as np
import random

inf = 999_999
def FloydWarshall(Graph, n):
    d = np.copy(Graph)
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if (d[j, i] + d[i, k]) < d[j, k]:
                    d[j, k] = (d[j, i] + d[i, k])
    return d

def generateWeightedGraph(n):
    if n == 0:
        G = np.array([[]])
        return G
    if n == 1:
        G = np.array([[0]])
        return G
    random_path = []
    for i in range(0, 48):
        random_path.append(random.randint(1, 150))
    random_path.append(inf)
    random_path.append(inf)
    prob = []
    for i in range(0, 48):
        prob.append(0.0125) # each random weight has equal chance of appearing
    prob.append(0.2) # infinite weight has a collective 40% chance to appear throughout the graph matrix
    prob.append(0.2)
    G = np.random.choice(random_path, size=(n, n), p=prob) # generate base matrix with random weights and infinity
    
    # the following loop ensures that the matrix is symmetrical
    # the matrix must be symmetrical because the graph is undirected
    k = 1
    for i in range(0, n):
        for j in range(k, n):
            G[j, i] = G[i, j]
        k += 1
        
    # following loop ensures that graph is simple (no loops; irreflexive)
    for i in range(0, n):
        G[i, i] = 0
        
    # following loop makes sure that generated graph is connected
    # it does so by finding rows that only contain 0 and inf and replacing one of the indices with a random valid weight
    # it then changes the corresponding [j,i] index to the same weight value
    for i in range(0, n):
        found_noninf = 0
        for j in range(0, n):
            if G[i, j] != inf and G[i, j] != 0:
                found_noninf = 1
        if found_noninf == 0:
            index_possibilities = []
            for x in range(0, n):
                if x != i:
                    index_possibilities.append(x)
            j_index = random.choice(index_possibilities)
            rand = random.randint(1, 150)
            G[i, j_index] = rand # replace index with valid weight
            G[j_index, i] = rand # replace corresponding symmetrical index
    
    return G

# this function only exists so that inf is printed instead of 999999
def printWeightedGraph(graph, n):
    for i in range(0, n):
        print("[ ", end = "")
        for j in range(0, n):
            if graph[i, j] == inf:
                print("inf ", end = "")
            else:
                if graph[i, j] >= 100:
                    print(graph[i, j], "", end = "")
                elif graph[i, j] >= 10 and graph[i, j] < 100:
                    print("", graph[i, j], "", end = "")
                else:
                    print(" ", graph[i, j], "", end = "")
        print("]")

n = int(input("Enter number of vertices: "))
G = generateWeightedGraph(n)
print("Randomly generated weighted graph and its shortest paths:")
printWeightedGraph(G, n)
print("\n")
shortest_paths = FloydWarshall(G, n)
print(shortest_paths)
print("\n")

G = np.array([[0, 4, 3, inf, inf, inf, inf, inf], [4, 0, 2, 5, inf, inf, inf, inf], [3, 2, 0, 3, 6, inf, inf, inf], [inf, 5, 3, 0, 1, 5, inf, inf], [inf, inf, 6, 1, 0, inf, 5, inf], [inf, inf, inf, 5, inf, 0, 2, 7], [inf, inf, inf, inf, 5, 2, 0, 4], [inf, inf, inf, inf, inf, 7, 4, 0]], dtype=int)
print("Predetermined weighted graph and its shortest paths:")
printWeightedGraph(G, 8)
print("\n")
shortest_paths = FloydWarshall(G, 8)
print(shortest_paths)