import json

def parse_edges(d, parent=None):
    edges = []
    for key, value in d.items():
        if parent is not None:
            edges.append((parent, key))
        if isinstance(value, dict):
            edges.extend(parse_edges(value, key))
    return edges

def json_to_edges(json_str):
    data = json.loads(json_str)
    edges = parse_edges(data)
    return edges

def edges_to_adjacency_matrix(edges):
    nodes = set()
    for edge in edges:
        nodes.update(edge)
    nodes = sorted(nodes)
    node_index = {node: index for index, node in enumerate(nodes)}
    
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    
    for edge in edges:
        start, end = edge
        matrix[node_index[start]][node_index[end]] = 1
    
    return matrix

def edges_to_adjacency_list(edges):
    adjacency_list = {}
    for start, end in edges:
        if start not in adjacency_list:
            adjacency_list[start] = []
        adjacency_list[start].append(end)
    return adjacency_list

input_str = """{
    "1": {
        "2": {
            "3": {
                "5": {},
                "6": {}
            },
            "4": {
                "7": {},
                "8": {}
            }
        }
    }
}"""

def main(input_str):
    edges = json_to_edges(input_str)
    print("Edges:", edges)
    adjacency_matrix = edges_to_adjacency_matrix(edges)
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)

    adjacency_list = edges_to_adjacency_list(edges)
    print("Adjacency List:")
    for node in sorted(adjacency_list):
        print(f"{node}: {adjacency_list[node]}")

main(input_str)