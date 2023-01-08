def get_vertical_stack(matrix_1: list, matrix_2: list) -> list:
    result = [[] for i in range(len(matrix_1) + len(matrix_2))]

    index_y = 0

    for matrix_1_index_y in range(len(matrix_1)):
        matrix_1_list_y = matrix_1[matrix_1_index_y]

        index_y = matrix_1_index_y

        for matrix_1_list_item_index_x in range(len(matrix_1_list_y)):
            result[index_y].append(matrix_1_list_y[matrix_1_list_item_index_x])

    for matrix_2_index_y in range(len(matrix_2)):
        matrix_2_list_y = matrix_2[matrix_2_index_y]

        index_y += 1

        for matrix_2_list_item_index_x in range(len(matrix_2_list_y)):
            result[index_y].append(matrix_2_list_y[matrix_2_list_item_index_x])

    return result

