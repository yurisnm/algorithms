#   Program to print BFS and DFS

#   defaultdict is a variation of dict that if the key doesn't exist it will be
# created and the value will be added, if it does exist it will be just added.
from collections import defaultdict

#   Graph store a graph using defaultdict that hold its edges and its adjacent
# edges as well.
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def add_edge_bidirectional(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, s):
        # all vertices not visited when start
        visited = defaultdict(bool)
        for k in self.graph:
            visited[k] = False

        # queue for BFS.
        # Here we keep adding non visited vertex and marking it
        # immediately as visited, so when we pop it in the future it won't be
        # added to the queue again since it has already been visited. This way
        # popping the zero index element we guarantee that the closest
        # vertexes will be visited first. so we have a BFS
        queue = []

        # the start point is marked as visited and the next vertex is passed.
        queue.append(s)
        visited[s] = True

        while queue:
            #dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=' ')
            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for v in self.graph[s]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

    def dfs(self, s):
        visited = defaultdict(bool)
        for k in self.graph:
            visited[k] = False

        stack = []

        stack.append(s)
        visited[s] = True
        print(s, end=' ')

        while stack:
            s = stack[-1]
            visited[s] = True
            all_visited = True
            for v in self.graph[s]:
                if not visited[v]:
                    stack.append(v)
                    print(v, end=' ')
                    all_visited = False
                    break
            if all_visited:
                stack.pop(-1)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
#0-→1
#⇅ ↙
#2-→3↻
#



g2 = Graph()
g2.add_edge_bidirectional('a', 'b')
g2.add_edge_bidirectional('b', 'c')
g2.add_edge_bidirectional('c', 'd')
g2.add_edge_bidirectional('d', 'a')

g2.add_edge_bidirectional('e', 'a')
g2.add_edge_bidirectional('e', 'b')
g2.add_edge_bidirectional('e', 'c')
g2.add_edge_bidirectional('e', 'd')
#bidirectional
#B---C
#|\ /|
#| E |
#|/ \|
#A---D

g2.dfs('a')








