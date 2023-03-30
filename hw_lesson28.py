"""
Task 1

Modify the `depth-first search` to produce strongly connected components (Strongly Connected Components ).
"""


class Vertex:

    def __init__(self, key):
        self.key = key  # int
        self.neighbors = {}  # {key: neighbor_vert}
        self.color = 'white'

    def add_neighbor(self, neighbor):
        self.neighbors[neighbor.key] = neighbor

    def __repr__(self):
        return f'V{self.key}'


class Graph:

    def __init__(self):
        self.vertices = {}  # key: Vertex(key)
        self.edges = []  # list of tuples (start, dest)

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, start, dest):
        if start not in self.vertices:
            self.add_vertex(start)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[start].add_neighbor(self.vertices[dest])
        self.edges.append((start, dest))

    def dfs(self, start: int, stack=None):
        if stack is None:
            stack = []
        current_vert = self.vertices[start]
        current_vert.color = 'gray'
        for neighbor_key, neighbor in self.vertices[start].neighbors.items():
            if neighbor.color == 'white':
                self.dfs(neighbor_key, stack)
        stack.append(start)
        return stack

    def transpose(self):
        g_t = Graph()
        for i in self.edges:
            g_t.add_edge(i[1], i[0])
        return g_t

    def find_scc(self, start):
        stack = self.dfs(start)
        trans = self.transpose()
        scc = []
        while stack:
            i = stack.pop()
            if trans.vertices[i].color == 'white':
                res = trans.dfs(i)
                scc.append(res)
        return scc

    def __repr__(self):
        return f'Graph: {self.vertices.keys()} | Edges: {self.edges}'


"""
Task 2

Using breadth-first search write an algorithm that can determine the shortest path
from each vertex to every other vertex. This is called the all-pairs shortest path problem.
"""


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()
        self.distance = 0

    def connect_to(self, neighbor):
        self.neighbors.add(neighbor)

    def __repr__(self):
        return f'V{self.key}'


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_edge(self, from_, to_):
        if from_ not in self.vertices:
            self.vertices[from_] = Vertex(from_)
        if to_ not in self.vertices:
            self.vertices[to_] = Vertex(to_)
        self.vertices[from_].connect_with(self.vertices[to_])
        self.edges.append((from_, to_))

    def bfs(self, start):
        queue = []
        visited = []
        start = self.vertices[start]
        start.distance = 0
        queue.append(start)
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in queue and neighbor not in visited:
                    neighbor.distance = current.distance + 1
                    queue.append(neighbor)
            visited.append(current)
        return {x: x.distance for x in visited}

    def all_pairs(self):
        for i in range(len(self.vertices)):
            print(f'Paths from V{i} - ', self.bfs(i))
