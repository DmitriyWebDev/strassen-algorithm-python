def get_normalized_matrices(matrix_1: list, matrix_2: list) -> (list, list):
    matrix_1_length = len(matrix_1)
    matrix_2_length = len(matrix_2)

    # Count max rows and cells

    max_matrix_rows = matrix_1_length if matrix_1_length >= matrix_2_length else matrix_2_length
    max_matrix_row_cells = 0

    for matrix_1_index_y in range(matrix_1_length):
        matrix_row_length = len(matrix_1[matrix_1_index_y])

        if matrix_row_length > max_matrix_row_cells: max_matrix_row_cells = matrix_row_length

    for matrix_2_index_y in range(matrix_2_length):
        matrix_row_length = len(matrix_2[matrix_2_index_y])

        if matrix_row_length > max_matrix_row_cells: max_matrix_row_cells = matrix_row_length

    # Validate and normalize max rows and cells count

    valid_max_matrix_rows = max_matrix_rows if max_matrix_rows % 2 == 0 else max_matrix_rows + max_matrix_rows % 2
    valid_max_matrix_row_cells = max_matrix_row_cells if max_matrix_row_cells % 2 == 0 else max_matrix_row_cells + max_matrix_row_cells % 2
    valid_matrix_size = valid_max_matrix_rows if valid_max_matrix_rows >= valid_max_matrix_row_cells else valid_max_matrix_row_cells

    # If matrices size valid return them

    are_matrices_valid = matrix_1_length == valid_matrix_size & matrix_2_length == valid_matrix_size

    if are_matrices_valid:
        for matrix_1_index_y in range(matrix_1_length):
            matrix_row_length = len(matrix_1[matrix_1_index_y])

            if matrix_row_length != valid_matrix_size:
                are_matrices_valid = False
                break

        for matrix_2_index_y in range(matrix_2_length):
            matrix_row_length = len(matrix_2[matrix_2_index_y])

            if matrix_row_length != valid_matrix_size:
                are_matrices_valid = False
                break

    if are_matrices_valid:
        return matrix_1, matrix_2

    # If matrices size invalid fix it

    result_matrix_1 = [[0 for i in range(valid_matrix_size)] for i in range(valid_matrix_size)]
    result_matrix_2 = [[0 for i in range(valid_matrix_size)] for i in range(valid_matrix_size)]

    for row_index in range(matrix_1_length):
        row = matrix_1[row_index]

        for row_item_index in range(len(row)):
            row_item = row[row_item_index]

            result_matrix_1[row_index][row_item_index] = row_item

    for row_index in range(matrix_2_length):
        row = matrix_2[row_index]

        for row_item_index in range(len(row)):
            row_item = row[row_item_index]

            result_matrix_2[row_index][row_item_index] = row_item

    return result_matrix_1, result_matrix_2
