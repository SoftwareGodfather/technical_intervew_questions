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
                    parent[child] = elem["data"]

    def DFS(self,root):
        print('DFS')
        parent = dict()
        stack = []
        stack.append(root)
        parent[root] = None
        while stack:
            elem = stack.pop()
            self.HandleElem(elem)
            for child in self.graph[elem]:
                if child not in parent.keys():
                    stack.append(child)
                    parent[child] = elem

# Driver program to test above functions 
g1 = Graph(5) 
g1.AddEdge(1, 0)
g1.AddEdge(0, 2)
g1.AddEdge(0, 3)
g1.AddEdge(2, 5)
g1.AddEdge(3, 4)
g1.AddEdge(0, 4)
g1.BFS(0)
g1.DFS(0)

########### STDOUT ###########

#BFS
#0
#1
#2
#3
#4
#DFS
#0
#3
#4
#2
#1
