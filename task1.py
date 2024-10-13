import networkx as nx
import matplotlib.pyplot as plt

# Створення графу.
G = nx.Graph()

# Додавання вершин (станцій).
stations = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(stations)

# Додавання ребер (маршрутів між станціями).
routes = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('C', 'F')]
G.add_edges_from(routes)

# Візуалізація графу.
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз графу.
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
average_degree = sum(degrees.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступені вершин: {degrees}")
print(f"Середній ступінь: {average_degree:.2f}")

# DFS та BFS обходи.
def dfs(graph, start, target, path=[]):
    path = path + [start]
    if start == target:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            new_path = dfs(graph, node, target, path)
            if new_path:
                return new_path
    return None

def bfs(graph, start, target):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == target:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None

# Застосування алгоритмів до графу.
start, target = 'A', 'F'
dfs_path = dfs(G, start, target)
bfs_path = bfs(G, start, target)

print(f"DFS шлях з {start} до {target}: {dfs_path}")
print(f"BFS шлях з {start} до {target}: {bfs_path}")

# Додавання ваг до ребер.
weighted_routes = [('A', 'B', 3), ('A', 'C', 2), ('B', 'D', 4), ('C', 'D', 1), ('D', 'E', 2), ('E', 'F', 3), ('C', 'F', 5)]
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_routes)

# Візуалізація графу з вагами.
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_weighted)
nx.draw(G_weighted, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G_weighted, 'weight')
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=labels)
plt.title("Транспортна мережа з вагами")
plt.show()

# Застосування алгоритму Дейкстри.
shortest_path = nx.dijkstra_path(G_weighted, 'A', 'F')
shortest_path_length = nx.dijkstra_path_length(G_weighted, 'A', 'F')

print(f"Найкоротший шлях з A до F: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_path_length}")

