import math

def calculate_entropy_for_graph(adjacency_list):
    """
    Рассчитывает энтропию графа на основе его списка смежности.
    
    :param adjacency_list: Словарь, представляющий список смежности графа (узел: список его соседей).
    :return: Энтропия графа.
    """
    # Шаг 1: Находим степень каждой вершины
    degrees = {node: len(neighbors) for node, neighbors in adjacency_list.items()}
    
    # Шаг 2: Находим общее количество ребер (или точнее, сумму всех степеней вершин)
    total_edges = sum(degrees.values())
    
    if total_edges == 0:
        return 0
    
    # Шаг 3: Высчитываем вероятность для каждой вершины и находим энтропию
    entropy = 0
    for node, degree in degrees.items():
        if degree > 0:
            probability = degree / total_edges
            entropy -= probability * math.log2(probability)
    
    return entropy


# Пример графа: список смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Расчет энтропии графа
graph_entropy = calculate_entropy_for_graph(graph)
print(f"Энтропия графа: {graph_entropy}")