import numpy as np
from math import log2
def enthropy(probabilities):
    return -sum([prob * log2(prob) for prob in np.nditer(probabilities)])

def main(input_matrix):
    # Нормируем матрику
    initial_matrix = np.array(input_matrix)
    amount_of_purchases = initial_matrix.sum()
    compatible_event_prob_matrix = initial_matrix / amount_of_purchases
    # Вычисляем вектор сумм по строчкам и по столбцам 
    p_y_vector = compatible_event_prob_matrix.sum(axis=1) 
    p_x_vector = compatible_event_prob_matrix.sum(axis=0) 
    
    # Вычисляем энтропию
    H_XY = enthropy(compatible_event_prob_matrix)
    H_Y = enthropy(p_y_vector)
    H_X = enthropy(p_x_vector)
    conditional_prob_matrix = np.copy(compatible_event_prob_matrix)
    overall_conditional_H = 0
    
    
    for row_index in range(len(compatible_event_prob_matrix)):
        # Берем условную вероятность строки
        conditional_prob_matrix[row_index] /= p_y_vector[row_index]
        # Берем энтропию строки
        conditional_H = enthropy(conditional_prob_matrix[row_index])    
        # Добавляем в общую условную энтрапию
        overall_conditional_H += conditional_H * p_y_vector[row_index]
    
    # Счиатем кол-во информации двумя методами
    information_quantity = H_X - overall_conditional_H
    H_XY_through_sum = H_Y + overall_conditional_H 
    
    print(f"I(X,Y) = Количество информации: {round(information_quantity, 2)}")
    print(f"H(XY) = Энтропия совместного события: {round(H_XY_through_sum, 2)}")

test_matrix = [[20, 15, 10, 5],
               [30, 20, 15, 10],
               [25, 25, 20, 15],
               [20, 20, 25, 20],
               [15, 15, 30, 25]]

main(test_matrix)