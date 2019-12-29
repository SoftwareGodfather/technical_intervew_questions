from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[1 for _ in range(V)] for _ in range(V)] 
    
    def PrintGraph(self):
        for i in range(self.V):
            print(self.graph[i])
            
    def MakePath(self, v, w):
        self.graph[v][w] = 0

    def Path(self, root):
        parent = dict()
        parent[root] = None
        queue = dequeue()
        queue.appendleft(root)
        while(queue):
            pass


# Driver program to test above functions 

g1 = Graph(5)
g1.MakePath(0, 0)
g1.MakePath(1, 0)
g1.MakePath(1, 1)
g1.MakePath(1, 2)
g1.MakePath(1, 3)
g1.MakePath(2, 3)
g1.MakePath(3, 3)
g1.MakePath(3, 4)

A = (0,0)
B = (3,4)
g1.Path(A, B)
