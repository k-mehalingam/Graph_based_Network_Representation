from typing import Dict, List
from Vertex import Vertex

"""
@Author: Karthikeyan Mehalingam
@Student Id: 801210897
@mail Id: kmehalin@uncc.edu
"""

class Graph:
    """A Class used to represent the Graph.

    ...

    Attributes
    ----------
    vertices: Dict
        a Dictionary to hold the vertices names and its objects.
    """

    def __init__(self):
        """ Initialize a empty dictionary to hold the vertices"""
        self.vertices: Dict[str: Vertex] = {}

    def add_edge(self, tail_vertex: str, head_vertex: str, weight: float) -> None:
        """
        adds a new edge to the graph.
        :param tail_vertex: source vertex
        :param head_vertex: destination vertex
        :param weight: the distance between tail and head vertex
        """

        # checking and creating a the head vertex if not present in the graph
        source = self.check_and_get_vertex(tail_vertex)

        # checking and creating a the tail vertex if not present in the graph
        destination = self.check_and_get_vertex(head_vertex)

        # checking and creating a new edge between the tail_vertex and head_vertex
        if destination.name not in source.adjacent_vertices:
            source.adjacent_vertices[destination.name] = []
        source.adjacent_vertices[destination.name] = [float(weight), True]

    def check_and_get_vertex(self, name: str) -> Vertex:
        """
        checks and creates and new vertex if not present in the vertices list
        :param name: name of the vertex.
        :return: object of the vertex
        """
        if name in self.vertices:
            return self.vertices[name]
        new_vertex = Vertex(name)
        self.vertices[name] = new_vertex
        return new_vertex

    def remove_edge(self, tail_vertex: str, head_vertex: str) -> None:
        """
        removes the edge between tail_vertex to head_vertex
        :param tail_vertex: name of the source vertex
        :param head_vertex: name of the destination vertex
        :return: None
        """
        # checking if the head vertex is present in the graph
        if head_vertex not in self.vertices:
            print("The given head vertex is not in the graph")
            return
        source = self.vertices[tail_vertex]

        # checking if a edge exists between the tail_vertex and head_vertex
        if head_vertex not in source.adjacent_vertices:
            print("there is no path between the given head and tail vertex")
        source.adjacent_vertices.pop(head_vertex)

    def print_graph(self) -> None:
        """
        prints the graph
        :return:
        """
        for vertex in sorted(self.vertices.keys()):
            if self.vertices[vertex].is_available is True:
                print(vertex)
            else:
                print(vertex+" DOWN")
            self.print_edges(self.vertices[vertex])
        print("")

    @staticmethod
    def print_edges(vertex: Vertex) -> None:
        """
        prints list of edges from the given vertex
        :param vertex: name of the vertex
        :return:
        """
        for edges in sorted(vertex.adjacent_vertices.keys()):
            if vertex.adjacent_vertices[edges][1] is True:
                print("\t"+edges+" "+str(vertex.adjacent_vertices[edges][0]))
            else:
                print("\t" + edges + " " + str(vertex.adjacent_vertices[edges][0])+" DOWN")

    def edge_down(self, tail_vertex: str, head_vertex: str) -> None:
        """
        marks the given edge from tail_vertex to head_vertex as down
        :param tail_vertex: name of the source vertex
        :param head_vertex: name of the head vertex
        :return:
        """
        if head_vertex not in self.vertices.keys():
            print("Given tail vertex is not in the graph")
            return
        if tail_vertex not in self.vertices.keys():
            print("Given head vertex is not in the graph")
            return
        v = self.vertices[tail_vertex]
        if head_vertex not in v.adjacent_vertices.keys():
            print("There is no route between the head and the tail vertex")
            return
        temp_arr = v.adjacent_vertices[head_vertex]
        temp_arr[1] = False
        v.adjacent_vertices[head_vertex] = temp_arr

    def edge_up(self, tail_vertex: str, head_vertex: str) -> None:
        """
        marks the given edge from tail to head vertex as up
        :param tail_vertex: name of the source vertex
        :param head_vertex: name of the destination vertex
        :return:
        """
        if head_vertex not in self.vertices.keys():
            print("Given tail vertex is not in the graph")
            return
        if tail_vertex not in self.vertices.keys():
            print("Given head vertex is not in the graph")
            return
        v = self.vertices[tail_vertex]
        if head_vertex not in v.adjacent_vertices.keys():
            print("There is no route between the head and the tail vertex")
            return
        temp_arr = v.adjacent_vertices[head_vertex]
        temp_arr[1] = True
        v.adjacent_vertices[head_vertex] = temp_arr
        return

    def vertex_up(self, vertex: str) -> None:
        """
        enables the given vertex in the graph for use.
        :param vertex: name of the vertex to enable
        :return:
        """
        if vertex not in self.vertices.keys():
            print("Given vertex is not in the graph")
            return
        v = self.vertices[vertex]
        v.is_available = True

    def vertex_down(self, vertex: str) -> None:
        """
        disables the given vertex in the graph for use.
        :param vertex:
        :return:
        """
        if vertex not in self.vertices.keys():
            print("Given vertex is not in the graph")
            return
        v = self.vertices[vertex]
        v.is_available = False

    def get_list_of_available_vertices(self) -> List[str]:
        """
        generates the list of vertices that are up for use.
        :return: list of vertices that are up.
        """
        result = []
        keys = self.vertices.keys()
        for key in keys:
            if self.vertices[key].is_available is True:
                result.append(key)
        return result

    def reset_vertices(self):
        """
        resets the previous vertex value in all vertices.
        :return:
        """
        for v in self.vertices:
            self.vertices[v].previous_vertex = ""
