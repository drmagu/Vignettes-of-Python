# Intro to undirected graphs

The main takeway of this vignette is that _graphs_ can be implemented with a _python dictionary_.  

The _keys_ of the _dictionary_ are the _nodes_ of our graph. The corresponding _values_ are _lists of nodes_, to which the _key node_ is connected.  

Example: 
```
graph1 = {
    'a': ['c', 'd'],
    'b': ['c', 'd'],
    'c': ['a', 'e'],
    'd': ['a', 'b'],
    'e': ['b', 'c'],
}
```
So there are 5 nodes, and 'a' is connected to 'c' and 'd', etc.  

With this backgound in mind, let us develop the Graph class.  

See *graph_class.py* for the implementation.  

## Graph class
* attributes
    * graph: a dictionary
    * nodes: a list of nodes
* methods
    * add_node(node) -> None
        * append the node to the nodes list
        * enter the node as a key in the graph with an empty list as values
    * add_edge(edge) -> None
        * parameter is edge, a tuple of nodes
        * nodes are added to the nodes list
        * the value for the keys in the graph is updated
    * show_edges() -> list
        * returns a list of tuples (the edges)
    * find_path(start, end) -> list
        * start and end are nodes
        * the path between them, if it exists, is a list of nodes with path[0] as start and path[len(path)-1] as end
        * if there is no path, None is returned
    * find_paths(start, end) -> list
        * start and end are nodes
        * a list of paths between start and end  
        * if there are no paths, None is returned  
    * find_all_paths() -> list
        * returns a list of all paths in the graph
        * returns None if there are no paths 
            * this only is possible when all values in the dictionary are an empty list
            * when there is only 1 node (hence not a graph)
    * shortest_path -> list
        * uses the min function on the all_paths list
    * longest_path -> list
        * uses the max function on the al_paths list
    * hamiltonian() -> bool
        * checks to see if the number of nodes in the longest path equals the number of nodes
            * if so, return True
            * if not, return False

## Notes on the implementation

### Hamiltonian
In the mathematical field of graph theory, a Hamiltonian path (or traceable path) is a path in an undirected or directed graph that visits each vertex exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a cycle that visits each vertex exactly once. 

A graph that contains a Hamiltonian Path (__HP__) is called a _traceable graph_.  

### Examples of non hamiltonian graphs
[Untraceable Graph](https://mathworld.wolfram.com/UntraceableGraph.html)

## Test and demo
See *graphs_demo.py*.  
Six graphs are presented, and various methods of the **Graph** class demonstrated.




