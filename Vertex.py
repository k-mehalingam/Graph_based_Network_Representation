from typing import Dict, List

"""
@Author: Karthikeyan Mehalingam
@Student Id: 801210897
@mail Id: kmehalin@uncc.edu
"""


class Vertex:
    """
    A class to represent a vertex in a graph.

    ....

    Attributes
    ----------
    name: str
        name of the vertex.
    adjacent_vertices: Dict[str: List[float, bool]]
        dictionary to hold the list of adjacent vertices from this.
    is_available: bool
        flag to show if the vertex is available or not.
    previous_vertex: str
        name of the previous vertex during any spt algorithms.
    """
    def __init__(self, name: str):
        self.name: str = name
        # Dict consisting of the weights and the availability of edges in the format
        # vertex_name: [weight, availability]
        self.adjacent_vertices: Dict[str: List[float, bool]] = {}
        self.is_available: bool = True
        self.previous_vertex: str = ""
