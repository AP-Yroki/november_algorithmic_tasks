array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def one_turn(matrix):
    size = len(matrix)
    current_size = size
    # Верхняя строка
    top_line = matrix[0]
    result = []
    result += top_line
    # Удалить верхнюю строку
    del matrix[0]
    # Правый столбец
    right_line = []
    for line in matrix:
        right_element = line[-1]
        right_line.append(right_element)
        del line[-1]
    result += right_line
    # Нижняя строка
    if not matrix:
        return result
    bottom_line = matrix[-1]
    result += reversed(bottom_line)
    del matrix[-1]
    # Левый столбец
    left_line = []
    for line in matrix:
        left_element = line[0]
        left_line.append(left_element)
        del line[0]
    result += reversed(left_line)

    return result


def view_matrix(matrix):
    result = one_turn(matrix)
    while matrix:
        result += one_turn(matrix)
    return result
print(view_matrix(array))