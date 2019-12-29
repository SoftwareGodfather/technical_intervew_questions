from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.N = N
        graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

# Driver program to test above functions 
g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4) 
print(g1.isTree())
  
g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 
print(g2.isTree())
