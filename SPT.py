from Graph import Graph
from Heap import MinHeap
from typing import List, Dict

"""
@Author: Karthikeyan Mehalingam
@Student Id: 801210897
@mail Id: kmehalin@uncc.edu
"""

class ShortestPathAlgorithms:
    """
    A class with the implementation of few shortest path algorithms.

    ....

    Attributes
    ----------
    obj: Graph
        the graph object on which the spt algorithms must be run.
    min_heap: MinHeap
        a Min heap for use in the spt algorithm
    """
    def __init__(self, obj: Graph):
        """
        initializes the class with the given object.
        :param obj: graph object.
        """
        self.graph = obj
        self.min_heap = MinHeap()

    def dijkstra_shortest_path_algorithm(self, source: str, destination: str) -> None:
        """
        implementation of dijkstra's algorithm to find the shortest path between a given source and destination
        prints the shortest path.
        :param source: name of the source
        :param destination: name of the destination.
        :return:
        """
        if source not in self.graph.vertices or self.graph.vertices[source].is_available is not True:
            print("the given source vertex is not in the graph or it is disabled")
            return
        if destination not in self.graph.vertices or self.graph.vertices[destination].is_available is not True:
            print("the given destination vertex is not in the graph or it is disabled")
            return

        # flag to note the visited nodes.
        node_visited = []

        # inserting all the vertices into the min heap.
        for v in self.graph.get_list_of_available_vertices():
            self.min_heap.insert_value(v, float('inf'))
        self.min_heap.update_distance(source, 0)
        final_distance = None
        while self.min_heap.size_of_heap() != 0:
            min_node = self.min_heap.extract_min()
            v = min_node[0]
            # updating the node as visited once extracted from min heap.
            node_visited.append(v)
            adj_vertices = self.graph.vertices[v].adjacent_vertices
            if destination == v:
                # stopping the algorithm once the destination vertex is reached and extracted from the min heap.
                final_distance = min_node[1]
                break
            # inserting the adjacent vertices of a vertex in the min heap.
            for adj_v in adj_vertices:
                if adj_vertices[adj_v][1] is False:
                    continue
                if self.min_heap.is_in_heap(adj_v):
                    new_dist = min_node[1] + adj_vertices[adj_v][0]
                    # updating the distance value of the vertex if new shortest path is found.
                    if new_dist < self.min_heap.get_node_from_heap(adj_v)[1]:
                        self.min_heap.update_distance(adj_v, min_node[1] + adj_vertices[adj_v][0])
                        # updating the previous vertex of the vertex.
                        self.graph.vertices[adj_v].previous_vertex = v
        # printing the traced shortest path from source to destination.
        self.trace_path(destination, final_distance)
        # resetting the vertices after the shortest path is found.
        self.graph.reset_vertices()

    def insert_adjacent_vertices(self, vertices: Dict[str, List]) -> None:
        """
        inserts the adjacent vertices of a given vertex into the min heap.
        :param vertices: list of adjacent vertices.
        :return:
        """
        for v in vertices:
            if vertices[v][1] is False:
                continue
            self.min_heap.insert_value(v, vertices[v][0])
        self.min_heap.build_min_heap()

    def trace_path(self, destination: str, distance: float):
        """
        prints the traced shortest path.
        :param destination: destination vertex.
        :param distance: computed shortest path distance.
        :return:
        """
        v = destination
        output_arr = []
        while v != "":
            output_arr.insert(0, v)
            v = self.graph.vertices[v].previous_vertex
        print(" ".join(output_arr) + " " + str(round(distance, 2)))
        print("")

    def reachability(self):
        """
        prints the list of vertices that are reachable from a given vertex.
        uses Breath First Search Algorithm to find the vertices that are reachable.
        Running time complexity is O(V + E), where V is the no of vertices and E is the no of edges in the graph.
        :return:
        """
        reachable_map = {}
        vertices_list = self.graph.get_list_of_available_vertices()
        for v in vertices_list:
            bfs_queue = list()
            bfs_queue.append(v)
            visited = list()
            while len(bfs_queue) != 0:
                vertex = bfs_queue.pop(0)
                adjacent_vertices = self.graph.vertices[vertex].adjacent_vertices
                for adv in adjacent_vertices:
                    if adjacent_vertices[adv][1] is False:
                        continue
                    if adv not in visited and self.graph.vertices[adv].is_available is True and adv != v:
                        visited.append(adv)
                        bfs_queue.append(adv)
            reachable_map[v] = visited
        for v in sorted(reachable_map.keys()):
            print(v)
            for a in sorted(reachable_map[v]):
                print("\t"+a)
        print("")
        return


