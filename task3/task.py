from math import log2
import json

def create_node(manager, subordinates):
    return {"manager": manager, "subordinates": subordinates}

def recursive_parse(manager, data, network):
    descendants = list(data.keys())
    for node, sub_data in data.items():
        if sub_data:
            network[node] = create_node(manager, recursive_parse(node, sub_data, network))
        else:
            network[node] = create_node(manager, [])
    return descendants

def json_to_network(json_string):
    network = {}
    data = json.loads(json_string)
    recursive_parse(None, data, network)
    return network

def get_colleagues(network, current_node):
    return [node for node in network if network[node]["manager"] == network[current_node]["manager"] and current_node != node]

def compute_ancestors(node, network):
    current = node
    count = 0
    while network[current]["manager"] is not None:
        count += 1
        current = network[current]["manager"]
    return count

def compute_indirect_subordinates(network, children, counter_ref):
    if not children:
        return
    for child in children:
        compute_indirect_subordinates(network, network[child]["subordinates"], counter_ref)
        counter_ref.count += 1

class Counter:
    count = 0

def compute_relationships(network):
    results = [[0 for _ in range(len(network))] for _ in range(5)]
    for current_node, details in network.items():
        results[0][int(current_node) - 1] = 1 if details["manager"] is not None else 0
        results[1][int(current_node) - 1] = len(details["subordinates"])
        results[2][int(current_node) - 1] = compute_ancestors(current_node, network) - 1 if details["manager"] is not None else 0
        colleagues = get_colleagues(network, current_node)
        counter_instance = Counter()
        for subordinate in network[current_node]["subordinates"]:
            compute_indirect_subordinates(network, network[subordinate]["subordinates"], counter_instance)
        results[3][int(current_node) - 1] = counter_instance.count
        results[4][int(current_node) - 1] = len(colleagues)
    return results

def compute_entropy(matrix):
    n = len(matrix[0])
    entropy_value = 0
    for column in zip(*matrix):
        partial_entropy = 0
        for value in column:
            if value != 0:
                probability = value / (n - 1)
                partial_entropy += probability * log2(probability)
        entropy_value += -partial_entropy
    return entropy_value

  

input_string = '''{
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
}
'''

network_structure = json_to_network(input_string)
relationship_matrix = compute_relationships(network_structure)
entropy_value = compute_entropy(relationship_matrix)
print(f"Значение энтропии: {round(entropy_value, 2)}")
