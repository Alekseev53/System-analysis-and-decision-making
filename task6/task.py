import json

def main(input_str, element_for_phasing):
    data = json.loads(input_str)
    print(data)
    return None

input_str = """{
    "комфортно": [
        [16, 0],
        [20, 1],
        [22, 1],
        [26, 0]
    ],
    "холодно": [
        [0, 1],
        [16, 1],
        [20, 0],
        [50, 0]
    ]
}"""

element_for_phasing = 17
main(input_str, element_for_phasing)