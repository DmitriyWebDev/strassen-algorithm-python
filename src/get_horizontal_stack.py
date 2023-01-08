def get_horizontal_stack(matrix_1: list, matrix_2: list) -> list:
    result = [[] for i in range(len(matrix_1))]

    for matrix_1_index_y in range(len(matrix_1)):
        matrix_1_list_y = matrix_1[matrix_1_index_y]
        matrix_1_list_y_length = len(matrix_1_list_y)

        for matrix_1_index_x in range(matrix_1_list_y_length):
            matrix_1_list_item = matrix_1_list_y[matrix_1_index_x]
            result[matrix_1_index_y].append(matrix_1_list_item)

        for matrix_2_index_x in range(matrix_1_list_y_length):
            matrix_2_list_item = matrix_2[matrix_1_index_y][matrix_2_index_x]
            result[matrix_1_index_y].append(matrix_2_list_item)

    return result
