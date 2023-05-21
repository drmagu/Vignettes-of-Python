
from copy import copy

class Graph:
    def __init__(self):
        self.graph = dict()
        self.nodes = []
        
    def add_node(self, node) -> None:
        if node not in self.nodes:
            self.nodes.append(node)
            self.graph[node] = []
        return

    def add_edge(self, edge: tuple) -> None:
        u, v = edge[0], edge[1]
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
        return

    def show_edges(self) -> list:
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges


    def find_path(self, start, end, path=None) -> list:
        if path is None:
            path = []
        path.append(start)   
        if start == end:
            return path
        neighbors = self.graph[start]
        for node in neighbors:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None
    
    def find_paths(self, start, end, path=None) -> list:
        if path is None:
            path = []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_paths(node, end, path[:])
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_all_paths(self) -> list:
        paths = []
        for node in self.nodes:
            for end in self.nodes:
                if end != node:
                    path = self.find_path(node, end)
                    paths.append(path)
        return paths

    def shortest_path(self) -> list:
        paths = self.find_all_paths()
        clean_paths = []
        if None in paths:
            for path in paths:
                if path is not None:
                    paths.remove(None)
                    clean_paths.append(path)
        else:
            clean_paths = paths
        return min(clean_paths, key=len)
    
    def longest_path(self) -> list:
        paths = self.find_all_paths()
        clean_paths = []
        if None in paths:
            for path in paths:
                if path is not None:
                    paths.remove(None)
                    clean_paths.append(path)
        else:
            clean_paths = paths
        return max(clean_paths, key=len)
    
    def hamiltonian(self) -> bool:
        if len(self.longest_path()) == len(self.nodes):
            return True
        return False
    

