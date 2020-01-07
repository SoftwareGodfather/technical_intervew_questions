import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def AddEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)


    def ShortestPath(self, root, nodeA):
        parent = dict()
        parent[root] =  None
        queue = collections.deque()
        queue.appendleft(root)
        while(queue):
            elem = queue.pop()
            if elem == nodeA:
                break
            for child in self.graph[elem]:
                if child not in parent.keys():
                    queue.appendleft(child)
                    parent[child] = elem
        
        path = []
        node = elem
        while(node != None):
            path.append(node)
            node = parent[node]
                
        return path

    def LastCommonAncestor(self, root, nodeA, nodeB):
        pathA = self.ShortestPath(root, nodeA)
        pathB = self.ShortestPath(root, nodeB)

        res = None
        while pathA and pathB:
            a = pathA.pop()
            b = pathB.pop()
            if a==b:
                res = a
        return res

g1 = Graph() 
g1.AddEdge(0, 1)
g1.AddEdge(0, 2)
g1.AddEdge(0, 3)
g1.AddEdge(2, 5)
g1.AddEdge(2, 6)
g1.AddEdge(3, 4)

print(g1.LastCommonAncestor(0,6,5))

#STDOUT
#2
