class Node:
    def __init__(self, name, weight):
        self.name = name       # Имя узла
        self.weight = weight   # Вес узла
        self.visited = False   # Флаг посещения узла

class Graph:
    def __init__(self):
        self.total_weight = 0    # Суммарный вес посещённых узлов
        self.nodes = []          # Список узлов графа
        self.adjacency_list = {} # Список смежности для представления рёбер

    def add_node(self, name, weight):
        node = Node(name, weight)
        self.nodes.append(node)
        index = len(self.nodes) - 1
        self.adjacency_list[index] = []  # Инициализируем список смежности для нового узла

    def add_edge(self, start_index, end_index):
        # Добавляем ребро в обе стороны для неориентированного графа
        self.adjacency_list[start_index].append(end_index)
        self.adjacency_list[end_index].append(start_index)

    def get_unvisited_adjacent(self, node_index):
        # Возвращает индекс непосещённого смежного узла
        for adjacent_index in self.adjacency_list[node_index]:
            if not self.nodes[adjacent_index].visited:
                return adjacent_index
        return -1  # Если нет непосещённых смежных узлов

    def display_node(self, node_index):
        # Выводит имя узла
        print(self.nodes[node_index].name, end=' ')

    def dfs(self, start_index=0):
        # Обход графа в глубину начиная с узла start_index
        stack = []
        self.nodes[start_index].visited = True
        self.display_node(start_index)
        self.total_weight += self.nodes[start_index].weight
        stack.append(start_index)
        while stack:
            current_index = stack[-1]
            unvisited_adjacent = self.get_unvisited_adjacent(current_index)
            if unvisited_adjacent == -1:
                stack.pop()
            else:
                self.nodes[unvisited_adjacent].visited = True
                self.display_node(unvisited_adjacent)
                self.total_weight += self.nodes[unvisited_adjacent].weight
                stack.append(unvisited_adjacent)
        # Сбрасываем флаг посещения для всех узлов
        for node in self.nodes:
            node.visited = False

# Создание графа и добавление узлов
graph = Graph()
graph.add_node('n0', 5)    # Узел 0
graph.add_node('n1', 2)    # Узел 1
graph.add_node('n2', 20)   # Узел 2
graph.add_node('n3', 1)    # Узел 3
graph.add_node('n4', 11)   # Узел 4

# Добавление рёбер
graph.add_edge(0, 1)
graph.add_edge(0, 2)    
graph.add_edge(0, 3)    
graph.add_edge(1, 4)    
graph.add_edge(2, 4)    
graph.add_edge(3, 4)    

# Запуск DFS и вычисление среднего веса
print("Обход графа в глубину (DFS):")
graph.dfs()
average_weight = graph.total_weight / len(graph.nodes)
print(f"\nСредний вес узлов: {average_weight}")
