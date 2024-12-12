import numpy as np
from math import log2

def calculate_entropy(probabilities):
    """Вычисляет энтропию на заданном массиве вероятностей."""
    entropy = -np.sum(probabilities * np.log2(probabilities, out=np.zeros_like(probabilities), where=(probabilities>0)))
    return entropy

def calculate_conditional_entropy(prob_matrix, marginal_probs):
    """Вычисляет условную энтропию."""
    conditional_entropy = 0
    for i, row in enumerate(prob_matrix):
        row_entropy = calculate_entropy(row / marginal_probs[i])
        conditional_entropy += row_entropy * marginal_probs[i]
    return conditional_entropy

def main(input_matrix):
    """Вычисляет энтропию совместного события и количество информации."""
    
    # Преобразуем входные данные в numpy массив и вычисляем общую сумму покупок
    initial_matrix = np.array(input_matrix)
    total_purchases = initial_matrix.sum()
    
    # Подсчитываем матрицу вероятностей совместных событий
    joint_prob_matrix = initial_matrix / total_purchases
    
    # Вычисляем предельные вероятности
    marginal_prob_y = joint_prob_matrix.sum(axis=1)
    marginal_prob_x = joint_prob_matrix.sum(axis=0)
    
    # Вычисляем энтропии различных распределений
    joint_entropy = calculate_entropy(joint_prob_matrix)
    entropy_y = calculate_entropy(marginal_prob_y)
    entropy_x = calculate_entropy(marginal_prob_x)
    
    # Вычисляем условную энтропию и количество информации
    conditional_entropy = calculate_conditional_entropy(joint_prob_matrix, marginal_prob_y)
    information_gain = entropy_x - conditional_entropy
    
    # Проверяем корректность расчета энтропии совместного события
    joint_entropy_via_sum = entropy_y + conditional_entropy
    
    print(f"Количество информации I(X,Y): {round(information_gain, 2)}")
    print(f"Энтропия совместного события H(XY): {round(joint_entropy_via_sum, 2)} (для обоих способов расчета)")

# По строкам находятся возрастные группы, по столбцам - категории товаров, в ячейке - количество товаров купленных определенной возрастной группой
test_matrix = [
    [20, 15, 10, 5],
    [30, 20, 15, 10],
    [25, 25, 20, 15],
    [20, 20, 25, 20],
    [15, 15, 30, 25]
]

main(test_matrix)