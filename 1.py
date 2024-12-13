import numpy as np

class Node:
    def __init__(self, name, weight):
        self.name = name       
        self.weight = weight  
        self.visited = False  

class Graph:
    def __init__(self):
        self.total_weight = 0              
        self.nodes = []                      
        self.adjacency_matrix = np.zeros((0, 0), dtype=bool)

    def add_node(self, name, weight):
        node = Node(name, weight)
        self.nodes.append(node)
        size = len(self.nodes)
        if size == 1:
            self.adjacency_matrix = np.zeros((1, 1), dtype=bool)
        else:
            self.adjacency_matrix = np.pad(self.adjacency_matrix, ((0,1),(0,1)), mode='constant', constant_values=False)

    def add_edge(self, start_index, end_index):
        self.adjacency_matrix[start_index][end_index] = True
        self.adjacency_matrix[end_index][start_index] = True

    def get_unvisited_adjacent_node_index(self, node_index):
        adjacent_indices = np.where(self.adjacency_matrix[node_index])[0]
        for adj_index in adjacent_indices:
            if not self.nodes[adj_index].visited:
                return adj_index
        return -1 

    def dfs(self, start_index=0):
        stack = []
        self.nodes[start_index].visited = True
        self.display_node(start_index)
        self.total_weight += self.nodes[start_index].weight
        stack.append(start_index)
        while stack:
            current_node_index = stack[-1]
            unvisited_adjacent_index = self.get_unvisited_adjacent_node_index(current_node_index)
            if unvisited_adjacent_index == -1:
                stack.pop()
            else:
                self.nodes[unvisited_adjacent_index].visited = True
                self.display_node(unvisited_adjacent_index)
                self.total_weight += self.nodes[unvisited_adjacent_index].weight
                stack.append(unvisited_adjacent_index)
        for node in self.nodes:
            node.visited = False

    def display_node(self, node_index):
        print(self.nodes[node_index].name, end=' ')

graph = Graph()
graph.add_node('A', 5)  
graph.add_node('B', 2)
graph.add_node('C', 20)
graph.add_node('D', 1) 
graph.add_node('E', 11) 

graph.add_edge(0, 1) 
graph.add_edge(1, 2)
graph.add_edge(2, 4) 
graph.add_edge(4, 3) 
graph.add_edge(3, 0) 

print("Обход графа в глубину (DFS):")
graph.dfs()
average_weight = graph.total_weight / len(graph.nodes)
print(f"\nСредний вес узлов: {average_weight}")
