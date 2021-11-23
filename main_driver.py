#!/usr/bin/python

##################################################
# Main file to run the graph program.
##################################################
"""
@Author: Karthikeyan Mehalingam
@Student Id: 801210897
@mail Id: kmehalin@uncc.edu
"""

from input_handler import *
import sys


def main():
    if len(sys.argv) < 2:
        print("no input file was given")
        return
    # file name to read the input from.
    input_file = sys.argv[1]

    # initializing an empty graph for use.
    graph = Graph()

    # function to parse input file and insert vertices and edges in graph
    parse_ip_file(input_file, graph)

    query_file = ""
    output_file = ""
    if len(sys.argv) >= 3:
        query_file = sys.argv[2]
    if len(sys.argv) >= 4:
        output_file = sys.argv[3]

    # redirecting to input fetching function.
    get_input_from_io(query_file, output_file, graph)


"""
call the main driver file in the given format
python main_driver.py input_file.txt queries.txt output_file.txt
"""
if __name__ == '__main__':
    main()
