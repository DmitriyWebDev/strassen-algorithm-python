def entrywise_subtract_two_matrices(matrix_1, matrix_2):
    matrix_size_x = len(matrix_1[0])
    matrix_size_y = len(matrix_1)

    result = [[0 for i in range(matrix_size_x)] for i in range(matrix_size_y)]

    for matrix_1_child_list_index in range(len(matrix_1)):
        matrix_1_child_list = matrix_1[matrix_1_child_list_index]

        for matrix_1_child_list_item_index in range(len(matrix_1_child_list)):
            matrix_1_child_list_item = matrix_1_child_list[matrix_1_child_list_item_index]
            matrix_2_child_list_item = matrix_2[matrix_1_child_list_index][matrix_1_child_list_item_index]

            result[matrix_1_child_list_index][matrix_1_child_list_item_index] = matrix_1_child_list_item - matrix_2_child_list_item

    return result
