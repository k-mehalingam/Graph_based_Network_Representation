# PROJECT 1
## Shortest Paths in a Network

##### Author
Karthikeyan Mehalingam  
801210897  
kmehalin@uncc.edu  

### Introduction:
This project is an approach to represent a Network using Graph Data Structure and to use Shortest Path Algorithms for finding the shortest paths between two nodes in a network. A Graph is a non-linear data structure that consists of vertices and edges. This can be used to represent a network with network components being the vertices and connections between the network components as edges. In this project, we will be using Dijkstra's Shortest path algorithm to find the shortest distance between two given nodes.

### Execution:
This project can be executed by calling the main_driver.py file with the input file consisting of the initial vertices and edges list along with the optional query and output file.

**python main_driver.py input_file.txt <query_file.txt> <output_file.txt>**  
Options: Enter 1 to give queries from console. 2 to use the queries from the file  
Input 1 - gets input queries from the user.  
Input 2 - takes queries from the query file.

##### Input File Format
The input file must be of the format  
**tail_vertex1 head_vertex1 distance  
tail_vertex2 head_vertex2 distance**

#### Query File Format:
The query file is optional and will be needed only when console input is not given. The query file must be of the format.

**query1 \<parameter1\> \<parameter2\>....\<parameter3\>  
query2 \<parameter1\> \<parameter2\>....\<parameter3\>**

#### List of Queries Supported:
The project supports the following list of queries that can be run on the graph.  
1. **print** - prints the entire graph.  
2. **path** from_vertex to_vertex - generates the shortest path from the from_vertex to to_vertex and prints the path along with the distance.  
3. **addedge** tail_vertex head_vertex distance - inserts a new edge in the graph with tail_vertex as start and head_vertex as end points with the mentioned distance as the weight of the edge.  
4. **deleteedge** tail_vertex head_vertex - deletes an edge in the graph running between the tail vertex and head_vertex.  
5. **edgedown** tail_vertex head_vertex - marks the edge between the tail_vertex and head_vertex as down. (if marked as edgedown, the edge will not be used for any shortest path calculation or reachability checks.)  
6. **edgeup** tail_vertex head_vertex - marks the edge between the tail_vertex and head_vertex as up.  
7. **vertexdown** vertex - marks the vertex as down. (if marked as down, the vertex will not be used for any shortest path calculation or reachability checks.)  
8. **vertexup** vertex - marks the vertex as up.  
9. **reachability** - prints the list of vertices which are accessible from every vertex in the graph.  
10. **quit** - Exits the program.

### Implementation Details:
In this project, The locations are considered as vertices of the graph and the path between two locations can be expressed as edges in the graph. Following are the list of classes and helper functions that are used in this project

#### List of Classes and Files:  
1. **main_driver.py**
        consists of the main method which is required to run the project.  
2. **input_handler.py**
        Consists of functions that are required to parse the input either from the console or to get the input from the query file and to set the output redirection to the specified file if output file name is given.  
3. **Vertex.py**  
        This file contains the implementation of the vertex data structure for the graph. It holds all the information that a vertex must hold, like the name of the vertex, the adjacency list, flag whethere the vertex is up/down, and the previous vertex when computing a shortest path.  
    **List of Attributes:**  
            **name**: str  
                name of the vertex.  
            **adjacent_vertices**: Dict[str: List[float, bool]]  
                dictionary to hold the list of adjacent vertices from this.  
                It has a List of 2 values, with the first value being the distance of the vertice and second being the status of the edge(up or down)  
            **is_available**: bool  
                flag to show if the vertex is available or not.  
            **previous_vertex**: str  
                name of the previous vertex during any spt algorithms.  
3. **Graph.py**  
        This file contains the main implementation details of the graph data structure and its required functions.  
    **List of Attributes:**  
            **vertices**: Dict - A Dictionary to hold the vertices names and its objects. Used to maintain the list of vertices in the graph.  

    **List of Functions:**  
            **add_edge(tail_vertex, head_vertex, distance)**  
                adds a edge to the graph. The head_vertex will be added in the adjacent vertices list of the tail vertex, if not present already. If the head_vertex is already present, then the distance value alone will be updated in it.  
            **delete_edge(tail_vertex, head_vertex)**  
                deletes the given edge from the graph. It will remove the head_vertex from the adjacent vertices list of the tail_vertex.  
            **check_and_get_vertex(name)**  
                checks if the given vertex is already present in the vertices list of the graph. It will return the vertex object if it is already present. If not it will create a new object and will return it.  
            **print_edges()**  
                Prints the entire graph in the below mentioned format.  
                Vertex1  
                    vertex2  
                    vertex3  
                    .  
                    .  
                Vertex2  
                    vertex3  
                    vertex4  
                    .  
                    .  
            **edge_down(tail_vertex, head_vertex)**  
                Marks the given edge from tail_vertex to head_vertex as down. when a given edge is marked as down, then this edge will not be used in the graph for shortest path calculation or to find the reachability of one vertice from another.  
            **edge_up(tail_vertex, head_vertex)**  
                Marks the given edge from tail_vertex to head_vertex as up. Once the edge is marked as up, then it will be used in all graph based operations.  
            **vertex_down(vertex)**  
            	Marks the given vertex as down so that it will not be used in the graph for traversal or computations.  
            **vertex_up(vertex)**  
            	Marks the given vertex as up so that it can be used in the grap for the traversals and computations.  
            **get_list_of_available_vertices()**  
            	returns the list of vertices which are up and can be used in the graph.  
            **reset_vertices()**  
            	Sets the value of the previous_vertex as empty. can be used after any traversal to reset the vertices.  
4. **Heap.py**  
		This file contains the implementation of the min heap which will be used for the calculation of the shortest path using Djikstra's Algorithm.  
	**List of Attributes:**  
		heap: List[List[str, float]] - The array used to represent the min heap for the implementation.  
		pos: Dict[str: int] - mapper used to map the index value of the vertices with its indexes in the heap.  
		
	**List of Functions:**  
		**new_node(vertex, distance)**  
			creates a new node to be inserted into the min heap.  
		**extract_min()**  
			extracts the minimum value from the heap, ie the root of the min_heap.  
		**min_heapify(index)**  
			run the min heap operation on the given index number.  
		**build_min_heap()**  
			builds the min heap with the values inserted into the heap.  
		**update_distance(name, val)**  
			updates the distance value for the given node inside the heap.  
		**swap_position_values(index1, index2)**  
			swaps the values between index1 and index2 in the heap.  
		**get_parent_index(index)**  
			returns the index of the parent for the ndoe in the given index.  
		**get_left_child(index)**  
			returns the index of the left child for the given node.  
		**get_right_child(index)**  
			returns the index of the right child for the given node.  
		**insert_value(name, distance)**  
			inserts a new node with the name and distance into the heap.  
		**print_heap()**  
			prints the values that are present in the heap.  
		**size_of_heap()**  
			returns the size of the heap.  
		**is_in_heap(name)**  
			checks if the given node is present in the heap or not.  
		**get_node_from_heap(name)**  
			gets the value of the node from the heap without deleteting the node.  
5. **SPT.py**  
	This file contains the implementation of the shortest path algorithms which are used in this project. In order to compute the shortest path between two vertices, Djikstra's algorithm is used. To get the list of Reachable vertices for a given vertex.  
	**List of Attributes:**  
		**graph** - object representing the graph in this project  
		**min_heap** - object containing the min_heap  
	**List of Functions:**  
		**djikstra_shortest_path_algorithm(source, destination)**  
			implementation of the shortest path calculation using the djikstra's algorithm. It uses the min heap to find the next vertex which is closer to the given source vertex in the graph.  
		**insert_adjacent_vertices(vertices)**  
			inserts the list of adjacent vertices of a given vertex into the min heap for the spt calculation.  
		**trace_path(destination, distance)**  
			prints the path traced from the source to the destination after finding the shortest path algorithm.  
		**reachability()**  
			returns the list of vertices which are reachable from every vertex.  

#### Djikstra's Shortest Path Algorithm:  
It is used to find the shortest path from a source vertex to destination in the graph. At every step of the algorithm we find the next nearest vertex with the smallest value of distance.  
	**Note:** The vertices and edges which are down will not be used in this algorithm  
##### Algorithm Steps:  
1. Insert all the vertices that are up into the min_heap with the distance value as infinity.  
2. Update the distance value of the source vertex as 0 in the min_heap.  
3. Extract the min value from the min heap.  
4. Based on the adjacent_vertices list of the vertex extracted from the min heap, calculate the new distance to each vertex by adding the edge weight and the value in the min heap.  
	new_distance = min_distance_from_heap + edge_weight  
5. If the new distance is less than the value in the value in the min heap, then update the distance value of the vertices and min_heapify the heap. If the value is updated, then update the previous_vertex value with the vertex extracted from the min heap.  
6. repeat steps from 3 to 5 until the destination node is extracted from the min heap.  
7. once the destination value is extracted, end the algorithm and call the trace_path function to print the path with the final distance computed.  
##### Time Complexity  
The time complexity of the Djikstra's shortest path algorithm is O(V + ElogV). Since all the vertices are visited a mininum of one time it takes O(V) and for every edge it traverses we use a flag to check if a vertex has been visisted or not, which uses a time of O(E logV). Hence the total Time complexity to find the shortest path using Djikstra's is O(V + ElogV).  

#### Reachability Algorithm:  
This algorithm is used to find the list of vertices that are reachable from a given vertex. This algorithms basically makes use of the Breath First Search Algorithm to find the list of reachable vertices from a given vertex. Hence we run the BFS for all the vertices that are present in the graph.   
	Note: The vertices and edges which are down will not be used in this algorithm.  
##### Algorithm Steps:  
1. Iterate throught the list of vertices which are up in the graph.  
2. For every vertices in the graph, run BFS and store the vertices which are traversed during the process.  
3. Repeat step 2 for all the vertices.  

##### BFS Algorithm:  
1. Initialize an empty queue.  
2. Insert the source vertex into the queue.  
3. Extract the first vertex in the queue.  
4. get the list of adjacent vertices that are present for the given node.  
5. check if the given node is already visited or not. If not visited, put it in the list of visited nodes.  
6. repeat steps 3 to 5 until the queue gets empty.  

##### Time Complexity Analysis:  
The time taken for the BFS algorithm to traverse throught the graph is O(V + E) where V is the no of vertices in the graph and E being the list of Edges present in the graph. Since we are running BFS for each vertex present in the graph, the total time complexity of the Reachability Algorithm is O(V(V + E))  

##### Compiler/Interpreter Used:  
This project can be run on any python interpreter. The testing of this project was done using **cpython** inpterpreter.  

##### Error Handling and Known Issues:  
* Approriate Error messages have been added for the following actions.  
    * deleteedge - when edge is not present between the given vertices.  
    * edgedown - when given edge is not present between the given vertices.  
    * edgeup - when given edge is not present between the given vertices.  
    * vertexup - when given vertex is not in the graph.  
    * vertexdown - when the given vertex is not in the graph.  
    * path - when the given source/destination vertex is not in the graph or in down state.  
* vertex names are case sensitive - eg: Belk and belk will be considered as two different vertices.  
* Program fails to throw error when negative distances are given between two vertices.  
* The heap is designed to work only as a min-heap(to solve the current requirement). Cannot be used as a max heap if needed.  

##### Future Works/Plans:  
* Currently the heap uses a array for the heap representation and a dictionary to store the position which takes a lot of space in terms of memory. Plans to optimize space usage by designing a better data structure for the min-heap implementation.  
* The algorithm to find the reachability of nodes requires to run the BFS on every vertices, which takes a running time of O(V(V+E)). This can be optimized by using memoization technique, where the reachability of a known vertex can be used if it is present in the adjacent vertices list of another vertex. ie, if Education, Duke are reachable from Belk, and Belk is reachable from Health, then it can be concluded that Education, Duke are also reachable from Health through Belk.  
