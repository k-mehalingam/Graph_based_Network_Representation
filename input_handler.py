import sys
from Graph import Graph
from SPT import ShortestPathAlgorithms

"""
Helper file with functions to help with I/O

@Author: Karthikeyan Mehalingam
@Student Id: 801210897
@mail Id: kmehalin@uncc.edu
"""

def parse_ip_file(file_path: str, obj: Graph) -> None:
    """
    parses a given input file and adds edges into the graph.
    :param file_path: file path of the ip file.
    :param obj: graph object
    :return:
    """
    file = open(file_path, "r")
    lines = file.readlines()
    for line in lines:
        line = line.split(" ")
        obj.add_edge(line[0], line[1], line[2])
        obj.add_edge(line[1], line[0], line[2])
    return


def process_query(query_string: str, graph: Graph):
    """
    processes a given query string and performs the respective action.
    :param query_string: query string from a file or console input
    :param graph: graph object.
    :return:
    """
    query_string = query_string.split(" ")
    if query_string[0] == "print":
        graph.print_graph()
    elif query_string[0] == "path":
        shortest_path = ShortestPathAlgorithms(graph)
        shortest_path.dijkstra_shortest_path_algorithm(query_string[1], query_string[2])
    elif query_string[0] == "edgedown":
        graph.edge_down(query_string[1], query_string[2])
    elif query_string[0] == "edgeup":
        graph.edge_up(query_string[1], query_string[2])
    elif query_string[0] == "vertexup":
        graph.vertex_up(query_string[1])
    elif query_string[0] == "vertexdown":
        graph.vertex_down(query_string[1])
    elif query_string[0] == "addedge":
        graph.add_edge(query_string[1], query_string[2], query_string[3])
    elif query_string[0] == "deleteedge":
        graph.remove_edge(query_string[1], query_string[2])
    elif query_string[0] == "reachable":
        reachability = ShortestPathAlgorithms(graph)
        reachability.reachability()
    else:
        print("Please give proper query")
    return


def get_input_from_io(query_file, output_file, graph: Graph):
    """
    gets input from user console.
    :param query_file: file path of the query file.
    :param output_file: file path of the output file.
    :param graph: graph object.
    :return:
    """
    while True:
        print("Enter 1 to give queries from console. 2 to use query from file")
        ip = input()
        if not ip.isdigit():
            print("Enter proper input.")
        else:
            break
    if int(ip) == 2:
        if query_file == "" or output_file == "":
            print("query file or output file name cannot be empty")
            return
        parse_query_file(query_file, output_file, graph)
    else:
        while True:
            print("Enter your query: \n1.print\n2.path <from_vertex> <to_vertex>\n3.edgedown <tailvertex> <headvertex>"
                  "\n4.edgeup <tailvertex> <headvertex>\n5.addedge <tailvertex> <headvertex> <distance>\n"
                  "6.deleteedge <tailvertex> <headvertex>\n7.vertexdown <vertex>\n8.vertexup <vertex>\n9.reachable"
                  "\n10.quit")
            query = input()
            if isinstance(query, str) is False:
                print("Enter query in proper format")
                continue
            if query == "quit":
                break
            process_query(query, graph)

    return


def parse_query_file(query_file, output_file, graph):
    """
    parses the given query file and calls the process_query function.
    :param query_file: file path of the query file.
    :param output_file: file path of the output file.
    :param graph: graph object
    :return:
    """
    file = open(query_file, "r")
    lines = file.readlines()
    sys.stdout = open(output_file, "w")
    for line in lines:
        process_query(line.strip(), graph)
    return
