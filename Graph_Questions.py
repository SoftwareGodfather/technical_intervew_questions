import collections

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = collections.defaultdict(list)

    def AddEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def HandleElemDict(self, elem):
        print(f'data:{elem["data"]}, level:{elem["level"]}')

    def HandleElem(self, elem):
        print(elem)

    def BFS(self, root):
        print('BFS')
        parent = dict()
        queue = collections.deque()
        queue.appendleft({'data':root,'level':0})
        parent[root] = None
        while queue:
            elem = queue.pop()
            self.HandleElemDict(elem)
            for child in self.graph[elem["data"]]:
                if child not in parent.keys():
                    childLevel = elem["level"] + 1
                    queue.appendleft({'data':child,'level':childLevel})
                    parent[child] = elem
                    
    def BFS_DetectCycle(self, root):
        print('\nBFS DetectCycle')
        visited = set()
        queue = collections.deque()
        queue.appendleft(root)
        while queue:
            elem = queue.pop()
            self.HandleElem(elem)
            if elem not in visited:
                visited.add(elem)
            else:
                print('Cycle')
            for child in self.graph[elem]:
                if child not in visited:
                    queue.appendleft(child)

    def DFS(self,root):
        print('\nDFS')
        parent = dict()
        stack = []
        stack.append(root)
        prev = None
        while stack:
            elem = stack.pop()
            self.HandleElem(elem)
            if elem not in parent.keys():
                parent[elem] = prev
            else:
                print('Cycle')
            for child in self.graph[elem]:
                if child not in parent.keys():
                    stack.append(child)
            prev = elem

    def IsGraph(self, root):
        print('\nIsGraph:')
        stack = []
        visited = set()
        stack.append(root)
        while(stack):
            elem = stack.pop()
            if elem not in visited:
                visited.add(elem)
            else:
                return False
            for child in self.graph[elem]:
                if child not in visited:
                    stack.append(child)
        return True 

# Driver program to test above functions 

g1 = Graph(5) 
g1.AddEdge(0, 1)
g1.AddEdge(0, 2)
g1.AddEdge(0, 3)
g1.AddEdge(2, 5)
g1.AddEdge(3, 4)
g1.AddEdge(1, 4)
g1.BFS(0)
g1.BFS_DetectCycle(0)
g1.DFS(0)
print(g1.IsGraph(0))

########### STDOUT ###########

#BFS
#data:0, level:0
#data:1, level:1
#data:2, level:1
#data:3, level:1
#data:4, level:2
#data:5, level:2

#BFS DetectCycle
#0
#1
#2
#3
#4
#5
#4
#Cycle

#DFS
#0
#3
#4
#1
#2
#5
#1
#Cycle

#IsGraph:
#False
