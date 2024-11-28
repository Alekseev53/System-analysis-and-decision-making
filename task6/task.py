import json

def fuzzify(value, fuzzy_set):
    """Фаззификация: вычисление степени принадлежности четкого значения нечетким множествам."""
    memberships = {}
    for term, points in fuzzy_set.items():
        membership = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            if x1 <= value <= x2:  # Линейная интерполяция между точками
                if x1 == x2:  # На случай вертикальной линии
                    membership = max(y1, y2)
                else:
                    membership = y1 + (y2 - y1) * (value - x1) / (x2 - x1)
                break
        memberships[term] = membership
    return memberships

def defuzzify(fuzzy_result, output_set):
    """Дефаззификация: преобразование нечеткого результата в четкое значение."""
    numerator = 0
    denominator = 0
    for term, degree in fuzzy_result.items():
        if degree > 0:  # Берем степень принадлежности > 0
            points = output_set[term]
            centroid = sum([x for x, y in points]) / len(points)  # Центр масс множества
            numerator += degree * centroid
            denominator += degree
    return numerator / denominator if denominator != 0 else 0

def main(input_str, regulator_str, transition_str, element_for_phasing):
    # Загрузка входных данных
    input_set = json.loads(input_str)
    regulator_set = json.loads(regulator_str)
    transition_map = json.loads(transition_str)
    
    # Фаззификация входного значения
    fuzzy_input = fuzzify(element_for_phasing, input_set)
    print("Фаззифицированное значение:", fuzzy_input)
    
    # Применение правил переходов
    fuzzy_output = {}
    for input_term, degree in fuzzy_input.items():
        if input_term in transition_map:
            output_term = transition_map[input_term]
            if output_term in fuzzy_output:
                fuzzy_output[output_term] = max(fuzzy_output[output_term], degree)  # Комбинирование
            else:
                fuzzy_output[output_term] = degree
    print("Результат с правил переходов:", fuzzy_output)
    
    # Дефаззификация результата
    crisp_output = defuzzify(fuzzy_output, regulator_set)
    print("Дефаззифицированное значение:", crisp_output)
    
    return crisp_output

# Исправленные данные
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
        [0, 0],
        [22, 0],
        [26, 1],
        [50, 1]
    ]
}"""

regulator = """{
    "слабо": [
        [0, 1],
        [6, 1],
        [10, 0],
        [20, 0]
    ],
    "умеренно": [
        [6, 0],
        [10, 1],
        [12, 1],
        [16, 0]
    ],
    "интенсивно": [
        [0, 0],
        [12, 0],
        [16, 1],
        [20, 1]
    ]
}"""

transition = """{
    "холодно": "интенсивно",
    "комфортно": "умеренно",
    "жарко": "слабо"
}"""

element_for_phasing = 19.3
main(input_str, regulator, transition, element_for_phasing)