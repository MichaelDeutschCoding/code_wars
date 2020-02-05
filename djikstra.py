from collections import defaultdict
    
class Graph:
    def __init__(self):
        self.edges = defaultdict(set)
        self.nodes = set()

    def add_edge(self, n1, n2, weight):
        """For adding bi-directional edges to a graph"""
        self.edges[n1].add((n2, weight))
        self.edges[n2].add((n1, weight))
        self.nodes.update((n1, n2))

    def one_direction(self, n1, n2, weight):
        """For addding single direction edge"""
        self.edges[n1].add((n2, weight))
        self.nodes.update((n1, n2))


    def djikstra(self, root, goal):
        if not root in self.nodes:
            print("That start location's not even on the map!")
            return False
        if not goal in self.nodes:
            print("That end location's not even on the map!")
            return False        
        distances = {node: float('inf') for node in self.nodes}
        parent = {node: None for node in self.nodes}
        distances[root] = 0
        stack = list(self.nodes)
        visited = set()
        while stack:
            current = None
            min_distance = float('inf')
            for n in stack:
                if distances[n] < min_distance:
                    current = n
                    min_distance = distances[n]
            
            if not current:
                print('No path found')
                return False
            if current == goal:
                path = []
                e = current
                while e != root:
                    path.insert(0, e)
                    e = parent[e]
                path.insert(0, root)
                print(path)
                return distances[current]
            stack.remove(current)
            visited.add(current)
            for edge in self.edges[current]:
                if edge[0] in visited:
                    continue
                new_dist = distances[current] + edge[1]
                if new_dist < distances[edge[0]]:
                    distances[edge[0]] = new_dist
                    parent[edge[0]] = current
        print('End of the line. No path found.')
        return False

    
edges = (
    ('A', 'B', 5), ('A', 'C', 10), ('A', 'E', 2),
    ('B', 'C', 2), ('B', 'D', 4), ('C', 'D', 7),
    ('C', 'F', 10), ('D', 'E', 3),
)

g = Graph()
for edge in edges:
    g.add_edge(*edge)


edges2 = (      #mathcs.emory.edu
    ('0', '1', 3), ('1', '7', 4), ('7', '2', 2), ('2','5',1), ('5', '6', 8),
    ('2','3', 6), ('3','4',1), ('3','0', 2), ('0', '8', 4), ('4', '8', 8)
)
g2 = Graph()
for edge in edges2:
    g2.add_edge(*edge)




edges3 = (       # web.cecs.pdx.edu
    ('1', '4', 5), ('1', '2', 2), ('4', '2', 5), ('4', '5', 58),
    ('2', '3', 14), ('3', '5', 34), ('2', '5', 4)
)
g3 = Graph()
for edge in edges3:
    g3.add_edge(*edge)


# One directional edges
# algorithms.tutorialhorizon.com
# https://algorithms.tutorialhorizon.com/weighted-graph-implementation-java/
g4 = Graph()
edges4 = (
    ('0', '1', 4), ('1', '3', 2), ('0', '2', 3),
    ('3', '4', 2), ('1', '2' ,5), ('2', '3', 7),
    ('4', '5', 6), ('4', '1', 4), ('4', '0', 4)
)
for edge in edges4:
    g4.one_direction(*edge)

print(g4.djikstra('0', '4'))
print(g4.djikstra('5', '4'))    # Should return False
print(g4.djikstra('4', '3'))