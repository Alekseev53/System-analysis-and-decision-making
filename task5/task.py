import numpy as np
def build_matrix(a):
    n = len(a)
    a = {a[i]-1:n-i for i in range(len(a))}
    print({a[i]:n-i for i in range(len(a))})
    A = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        for j in range(n):
            if a[i] >= a[j]:
                A[i][j] = 1
            else:
                A[i][j] = 0
    
    return A

def main():
    # Пример
    a = [3, 1, 2]
    A = build_matrix(a)
    b = [1, 3, 2]
    B = build_matrix(b)
    # 2. Транспонирование матриц A и B
    A_T = A.T
    B_T = B.T

    Y_AB = A & B
    Y_AB_T = A_T & B_T
    K = Y_AB + Y_AB_T

    Y_AB = np.bitwise_and(A, B)

    # 3. Поэлементное "И" для A_T & B_T
    Y_AB_T = np.bitwise_and(A_T, B_T)

    # 4. Поэлементное сложение матриц Y_AB и Y_AB_T
    K = Y_AB + Y_AB_T

    # Вывод результатов
    print("Матрица A:")
    print(A)

    print("\nМатрица B:")
    print(B)

    print("\nМатрица Y_AB (A & B):")
    print(Y_AB)

    print("\nТранспонированная матрица A_T:")
    print(A_T)

    print("\nТранспонированная матрица B_T:")
    print(B_T)

    print("\nМатрица Y_AB_T (A_T & B_T):")
    print(Y_AB_T)

    print("\nИтоговая матрица K (Y_AB + Y_AB_T):")
    print(K)


    from collections import defaultdict, deque

    def find_ordering(pairs, n):
        # Строим граф зависимости
        graph = {i: [] for i in range(1, n+1)}  # создает пустые списки
        in_degree = {i: 0 for i in range(1, n+1)}  # степень вершин
        
        for i, j in pairs:
            graph[i].append(j)
            in_degree[j] += 1
        
        # Ищем вершины с 0 степенью
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        result = []
        visited = 0
        
        while queue:
            node = queue.popleft()
            result.append(node)
            visited += 1
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Если не удается добавить все вершины, значит есть цикл
        if visited != n:
            print("Граф имеет цикл, невозможно построить правильную аранжировку")
            return None
        
        return result

    # Извлекаем позиции с нулями из матрицы K и строим список пар (i+1, j+1)
    zero_pairs = []
    for i in range(len(K)):
        for j in range(i,len(K[0])):
            if K[i][j] == 0:
                zero_pairs.append((i+1, j+1))

    print("Список пар (i, j), где K[i][j] = 0:", zero_pairs)

    # Находим аранжировку (упорядоченную последовательность рангов)
    n = len(K)
    ordering = find_ordering(zero_pairs, n)

    print("Упорядоченная последовательность:", ordering)

main()