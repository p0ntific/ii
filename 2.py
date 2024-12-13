
import numpy as np

ROUND_NUM = 5
INFLUENCE_FACTOR = 0.1

class Graph:
    def __init__(self):
        self.labels = []
        self.values = np.array([], dtype=float)
        self.adjacency_matrix = np.zeros((0, 0), dtype=int)
    
    def add_vertex(self, label, value):
        self.labels.append(label)
        self.values = np.append(self.values, value)
        size = len(self.labels)
        if size == 1:
            self.adjacency_matrix = np.zeros((1, 1), dtype=int)
        else:
            self.adjacency_matrix = np.pad(self.adjacency_matrix, ((0,1), (0,1)), 'constant')

    def add_edge(self, start, end):
        for [i, j] in ((start,end), (end,start)):
            print(i,j)
            self.adjacency_matrix[i][j] = 1

    def update_vertex_states(self):
        degrees = np.sum(self.adjacency_matrix, axis=1)
        print(degrees)
        deltas = INFLUENCE_FACTOR * (self.adjacency_matrix.dot(self.values) - degrees * self.values)
        self.values += deltas

    def is_any_converged(self):
        rounded_values = np.round(self.values, ROUND_NUM)
        return np.all(rounded_values == rounded_values[0])
    
    def printMatrix(self):
        for row in self.adjacency_matrix:
            print(row)

    def printValues(self):
        print(self.values)

def main():
    graph = Graph()
    graph.add_vertex('A', 5)
    graph.add_vertex('B', 2)
    graph.add_vertex('C', 20)
    graph.add_vertex('D', 1)
    graph.add_vertex('E', 11)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 0)

    graph.printMatrix()

    iteration = 0
    while not graph.is_any_converged():
        graph.update_vertex_states()
        iteration += 1
        print(f'шаг {iteration}',end=' ')
        graph.printValues()


    result = round(graph.values[0], 3)

    print(f"Значение: {result}")

if __name__ == '__main__':
    main()
