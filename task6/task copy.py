import json

def main(input_str, element_for_phasing):
    data = json.loads(input_str)
    print(data)
    return None

input_str = """{
    "холодно": [
        [0, 1],
        [16, 1],
        [20, 0],
        [50, 0]
    ],
    "комфортно": [
        [16, 0],
        [20, 1],
        [22, 1],
        [26, 0]
    ],
    "жарко": [
        [0,0],
        [22,0],
        [26,1],
        [50,1],
    ]
}"""

regulator = """
{
    "слабо":[[0,1],[6,1],[10,0],[20,0]],
    "умеренно":[[6,0],[10,1],[12,1],[16,0]],
    "унтенсивно":[[0,0],[12,0],[16,1],[20,1]],
}
"""

transition = """
{
    'холодно':"унтенсивно",
    'комфортно':"умеренно",
    'жарко':"слабо"
}
"""

element_for_phasing = 17
main(input_str, element_for_phasing)