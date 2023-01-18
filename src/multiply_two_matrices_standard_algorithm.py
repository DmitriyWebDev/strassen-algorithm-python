def multiply_two_matrices_standard_algorithm(matrix_1: list, matrix_2: list) -> list:
    matrix_size_x = len(matrix_1[0])
    matrix_size_y = len(matrix_1)

    result = [[0 for i in range(matrix_size_x)] for i in range(matrix_size_y)]

    for matrix_1_index_y in range(len(matrix_1)):
        matrix_1_list = matrix_1[matrix_1_index_y]

        for matrix_1_index_x in range(len(matrix_1_list)):

            for item_index in range(len(matrix_1_list)):
                matrix_1_item = matrix_1_list[item_index]
                matrix_2_item = matrix_2[item_index][matrix_1_index_x]

                result[matrix_1_index_y][matrix_1_index_x] += matrix_1_item * matrix_2_item

    return result
