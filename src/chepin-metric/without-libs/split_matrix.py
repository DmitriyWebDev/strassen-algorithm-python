def split_matrix(matrix):
    res_1 = []
    res_2 = []
    res_3 = []
    res_4 = []

    x_divider_index = int(len(matrix[0]) / 2) - 1
    y_divider_index = int(len(matrix) / 2) - 1

    for y_item_index in range(len(matrix)):
        current_src_list = matrix[y_item_index]
        y_is_exceed_divider = y_item_index > y_divider_index

        for x_item_index in range(len(current_src_list)):
            current_item = current_src_list[x_item_index]

            x_is_exceed_divider = x_item_index <= x_divider_index

            target_list = []

            if not y_is_exceed_divider and not x_is_exceed_divider:
                target_list = res_2
            elif not y_is_exceed_divider and x_is_exceed_divider:
                target_list = res_1
            elif y_is_exceed_divider and not x_is_exceed_divider:
                target_list = res_4
            elif y_is_exceed_divider and x_is_exceed_divider:
                target_list = res_3

            if len(target_list) == 0:
                target_list.append([])

            last_item_sub_list = target_list[-1]

            if len(last_item_sub_list) == 2:
                target_list.append([])

            added_last_item_sub_list = target_list[-1]
            added_last_item_sub_list.append(current_item)

    return [res_1, res_2, res_3, res_4]

