from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[1 for _ in range(V)] for _ in range(V)] 
    
    def PrintGraph(self):
        for i in range(self.V):
            print(self.graph[i])
        print()
            
    def MakePath(self, v, w):
        self.graph[v][w] = 0

    def GetNext(self, elem):
        nextSteps = []
        if((elem[0] - 1) >= 0) and (self.graph[elem[0]-1][elem[1]] == 0):
            nextSteps.append((elem[0] - 1, elem[1]))
        if((elem[0] + 1) < self.V) and (self.graph[elem[0]+1][elem[1]] == 0):
            nextSteps.append((elem[0] + 1, elem[1]))
        if((elem[1] - 1) >= 0) and (self.graph[elem[0]][elem[1]-1] == 0):
            nextSteps.append((elem[0], elem[1] - 1))
        if((elem[1] + 1) < self.V) and (self.graph[elem[0]][elem[1]+1] == 0):
            nextSteps.append((elem[0], elem[1] + 1))
        return nextSteps

    def Path(self, A, B):
        print(f'Find Path from {A} to {B}')
        parent = dict()
        parent[A] = None
        queue = deque()
        queue.appendleft(A)
        while(queue):
            elem = queue.pop()
            if(elem == B):
                print('Path found!!!')
                return parent
            nextSteps = self.GetNext(elem)
            for nextStep in nextSteps:
                if nextStep not in parent:
                    queue.appendleft(nextStep)
                    parent[nextStep] = elem
        
        print('Path NOT found!!!')
        return None


# Driver program to test above functions 

g1 = Graph(5)
g1.MakePath(0, 0)
g1.MakePath(1, 0)
g1.MakePath(1, 1)
g1.MakePath(2, 1)
g1.MakePath(3, 1)
g1.MakePath(4, 1)
g1.MakePath(4, 0)
g1.MakePath(4, 3)
g1.MakePath(1, 2)
g1.MakePath(1, 3)
g1.MakePath(2, 3)
g1.MakePath(3, 3)
g1.MakePath(3, 4)
g1.PrintGraph()

A = (0,0)
B = (3,4)
parentList = g1.Path(A, B)
path = B
while(path):
    print(path)
    path = parentList[path]

########### STDOUT ###########
