class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

def add_edge(parent, child):
    parent.children.append(child)
    child.parent = parent

def get_all_ancestors(node):
    ancestors = set()
    current = node.parent
    while current:
        ancestors.add(current)
        current = current.parent
    return ancestors

def get_all_descendants(node):
    descendants = set()
    stack = [node]
    while stack:
        current = stack.pop()
        for child in current.children:
            descendants.add(child)
            stack.append(child)
    return descendants

# Определение отношений
def r1_direct_management(node):
    return set(node.children)

def r2_direct_subordination(node):
    return {node.parent} if node.parent else set()

def r3_indirect_management(node):
    all_descendants = get_all_descendants(node)
    return all_descendants - r1_direct_management(node)

def r4_indirect_subordination(node):
    all_ancestors = get_all_ancestors(node)
    return all_ancestors - r2_direct_subordination(node)

def r5_peer_subordination(node):
    if not node.parent:
        return set()
    siblings = set(node.parent.children)
    siblings.discard(node)
    return siblings

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
    results[node.value] = {
        "r1_direct_management": len(r1_direct_management(node)),
        "r2_direct_subordination": len(r2_direct_subordination(node)),
        "r3_indirect_management": len(r3_indirect_management(node)),
        "r4_indirect_subordination": len(r4_indirect_subordination(node)),
        "r5_peer_subordination": len(r5_peer_subordination(node))
    }

# Вывод результатов
print(f"{'Node':<3}{'r1_direct_management':<20} {'r2_direct_subordination':<20} {'r3_indirect_management':<20} {'r4_indirect_subordination':<20} {'r5_peer_subordination':<20}")
for node, info in results.items():
    print(f"{node:<3} {str(info['r1_direct_management']):<20} {str(info['r2_direct_subordination']):<20} {str(info['r3_indirect_management']):<20} {str(info['r4_indirect_subordination']):<20} {str(info['r5_peer_subordination']):<20}")