class Graph:
    def __init__(self, n_vertices, graph_type = 'undirected', weighted = False):
        self.n_vertices = n_vertices
        self.n_edges = 0
        self.graph_type = graph_type
        self.weighted = weighted
        self.edges = [[] for _ in range(n_vertices + 1)]
        
    def add_edge(self, u, v, weight = 1):
        if u < 0 or u >= self.n_vertices or v < 0 or v >= self.n_vertices:
            raise ValueError(f"Vertex index out of bounds: u={u}, v={v}")
        
        if self.weighted:
            self.edges[u].append((v, weight))
            if self.graph_type == 'undirected':
                self.edges[v].append((u, weight))
        else:
            self.edges[u].append(v)
            if self.graph_type == 'undirected':
                self.edges[v].append(u)
        
        self.n_edges += 1
        
    def add_edges(self, edge_list):
        for edge in edge_list:
            if self.weighted:
                u, v, weight = edge
                self.add_edge(u, v, weight)
            else:
                u, v = edge
                self.add_edge(u, v)
        
    def get_neighbors(self, u):
        if u < 0 or u >= self.n_vertices:
            raise ValueError(f"Vertex index out of bounds: u={u}")
        return self.edges[u]
    
    def get_all_edges(self):
        all_edges = []
        for u in range(self.n_vertices):
            for edge in self.edges[u]:
                if self.weighted:
                    v, weight = edge
                    all_edges.append((u, v, weight))
                else:
                    all_edges.append((u, edge))
        return all_edges
    
    def get_vertices(self):
        return list(range(self.n_vertices))
    
    def __str__(self):
        result = []
        for i in range(self.n_vertices):
            if self.weighted:
                edges_str = ', '.join([f"{v}(weight={w})" for v, w in self.edges[i]])
            else:
                edges_str = ', '.join(map(str, self.edges[i]))
            result.append(f"{i}: {edges_str}")
        return "\n".join(result)
    