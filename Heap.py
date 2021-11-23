from typing import List, Dict

"""
@Author: Karthikeyan Mehalingam
@Student Id: 801210897
@mail Id: kmehalin@uncc.edu
"""

class MinHeap:
    """
    A class to represent MinHeap

    ....

    Attributes
    ----------
    heap: List[List[str, float]]
        the min heap which holds the nodes.
    pos: Dict
        dictionary to hold the position of each node in the heap
    """

    def __init__(self):
        self.heap = []
        self.pos: Dict[str, int] = {}

    @staticmethod
    def new_node(vertex, distance) -> List:
        """
        generates a new node with a given name and distance
        :param vertex: name of the vertex
        :param distance: distance from the source
        :return: node of format List[name, distance]
        """
        node = [vertex, distance]
        return node

    def extract_min(self) -> List:
        """
        extracts the min value from the heap and returns it
        :return: min node
        """

        # check if heap is empty
        if len(self.heap) == 0:
            return None

        # popping the root node and replacing with last node.
        root_node = self.heap[0]
        self.pos.pop(root_node[0])
        last_node = self.heap[len(self.heap) - 1]
        self.heap[0] = last_node
        self.pos[last_node[0]] = 0
        self.heap.pop(len(self.heap) - 1)
        self.min_heapify(0)
        return root_node

    def min_heapify(self, index: int) -> None:
        """
        performs min_heapify operation on the heap at the given index
        :param index: index at which min_heapify is to be performed.
        :return:
        """
        heap_size = len(self.heap)
        l_index = self.get_left_index(index)
        r_index = self.get_right_index(index)
        smallest = None
        if l_index < heap_size and self.heap[l_index][1] < self.heap[index][1]:
            smallest = l_index
        else:
            smallest = index
        if r_index < heap_size and self.heap[r_index][1] < self.heap[smallest][1]:
            smallest = r_index
        if smallest != index:
            self.swap_position_values(smallest, index)
            self.min_heapify(smallest)

    def build_min_heap(self):
        """
        builds the min heap with the nodes present in the heap.
        :return:
        """
        heap_size = len(self.heap)
        for i in range((heap_size-1)//2, -1, -1):
            self.min_heapify(i)

    def update_distance(self, name: str, val: float) -> None:
        """
        updates the  distance of a node with the given value
        :param name: name of the vertex
        :param val: new distance to be updated.
        :return:
        """
        position = self.pos[name]
        self.heap[position][1] = val
        while position > 0 and self.heap[position][1] < self.heap[self.get_parent_index(position)][1]:
            self.swap_position_values(position, self.get_parent_index(position))
            position = self.get_parent_index(position)

    def swap_position_values(self, id1: int, id2: int):
        """
        swaps the position of the nodes in the given two indices.
        :param id1: index of node 1
        :param id2: index of node 2
        :return:
        """
        self.pos[self.heap[id1][0]], self.pos[self.heap[id2][0]] = self.pos[self.heap[id2][0]], \
                                                                   self.pos[self.heap[id1][0]]
        self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1]

    @staticmethod
    def get_parent_index(index: int) -> int:
        """
        generates the index of parent for the given node's index.
        :param index: index of current node.
        :return: index of parent node.
        """
        return (index - 1) // 2

    @staticmethod
    def get_left_index(index: int) -> int:
        """
        generates the index of left child from the given node's index.
        :param index: index of current node.
        :return: index of left child.
        """
        return 2 * index + 1

    @staticmethod
    def get_right_index(index: int) -> int:
        """
        generates the index of the right child from the given node's index.
        :param index:
        :return:
        """
        return 2 * index + 2

    def insert_value(self, name: str, distance: float) -> None:
        """
        inserts a new node into the heap.
        :param name: name of the node.
        :param distance: distance of the node from the source.
        :return:
        """
        node = self.new_node(name, distance)
        self.heap.append(node)
        self.pos[name] = len(self.heap) - 1

    def print_heap(self) -> None:
        """
        prints all the nodes and its values in the heap.
        :return:
        """
        for node in self.heap:
            print(node[0] + " " + str(node[1]))

    def size_of_heap(self) -> int:
        """
        returns the size of the heap.
        :return: size of the heap
        """
        return len(self.heap)

    def is_in_heap(self, name: str) -> bool:
        """
        checks if the given node is in the heap.
        :param name: name of the node.
        :return:
        """
        return True if name in self.pos else False

    def get_node_from_heap(self, name: str) -> bool:
        """
        gets the node with given name.
        :param name: name of the node.
        :return: returns the node with the name.
        """
        if name in self.pos:
            return self.heap[self.pos[name]]
        else:
            None




