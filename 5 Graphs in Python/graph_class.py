
from typing import Optional, List, Any

class Graph:
    """
    This class represents a simple undirected graph using an adjacency list.
    """
    def __init__(self):
        """
        Constructor of the Graph class.
        """
        self.graph = dict()
        self.nodes = []

    def add_node(self, node: str) -> None:
        """
        Method to add a node to the graph.
        """
        if node not in self.nodes:
            self.nodes.append(node)
            self.graph[node] = []
        return

    def add_edge(self, edge: tuple) -> None:
        """
        Method to add an edge to the graph. Edge is a tuple of two nodes.
        """
        u, v = edge[0], edge[1]
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
        return

    def get_edges(self) -> List[tuple]:
        """
        Method to get all edges of the graph.
        """
        return [(node, neighbor) for node in self.graph for neighbor in self.graph[node]]

    def find_path(self, start: str, end: str, path: Optional[List[str]] = None) -> Optional[List[str]]:
        """
        Recursive method to find a path from 'start' to 'end'.
        """
        if path is None:
            path = []
        path.append(start)

        if start == end:
            return path
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None
    
    def find_paths(self, start, end, path=None) -> list:
        """
        Method to find all paths from 'start' to 'end'.
        """
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

    def find_all_paths(self) -> List[List[Any]]:
        """
        Finds all possible paths between each pair of nodes in the graph.
        
        Returns:
            List of lists, where each list represents a path in the graph.
        """
        all_paths = []
        for start_node in self.nodes:
            for end_node in self.nodes:
                if start_node != end_node:
                    path = self.find_path(start_node, end_node)
                    if path is not None:
                        all_paths.append(path)
        return all_paths

    def shortest_path(self) -> Optional[List[str]]:
        """
        Method to find the shortest path from in the graph.
        """
        all_paths = self.find_all_paths()
        return min(all_paths, key=len, default=None)

    def longest_path(self) -> Optional[List[str]]:
        """
        Method to find the longest path from 'start' to 'end'.
        """
        all_paths = self.find_all_paths()
        return max(all_paths, key=len, default=None)

    def is_hamiltonian(self) -> bool:
        """
        Method to check if the graph is Hamiltonian. 
        It checks if the longest path includes all the nodes.
        """
        if len(self.longest_path()) == len(self.nodes):
            return True
        return False
