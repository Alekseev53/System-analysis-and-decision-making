"""
Дан граф
Для каждого узла братьев (все вершины имеющих общего предка с этой вершиной)
Для каждого узла всех его потомков
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_edge(parent, child):
    parent.children.append(child)

def get_siblings(node, root):
    siblings = set()
    stack = [root]
    while stack:
        current = stack.pop()
        for child in current.children:
            if node in current.children and child != node:
                siblings.add(child)
            stack.append(child)
    return siblings

def get_descendants(node):
    descendants = set()
    stack = [node]
    while stack:
        current = stack.pop()
        for child in current.children:
            descendants.add(child)
            stack.append(child)
    return descendants

# Построим дерево
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

add_edge(A, B)
add_edge(A, C)
add_edge(B, D)
add_edge(B, E)
add_edge(C, F)
add_edge(C, G)

nodes = [A, B, C, D, E, F, G]
results = {}

for node in nodes:
    siblings = get_siblings(node, A)
    descendants = get_descendants(node)
    results[node.value] = {
        "siblings": {sibling.value for sibling in siblings},
        "descendants": {descendant.value for descendant in descendants}
    }

# Вывод результатов
print(f"{'Node':<3} {'Siblings':<20} {'Descendants':<20}")
for node, info in results.items():
    print(f"{node:<3} {str(info['siblings']):<20} {str(info['descendants']):<20}")