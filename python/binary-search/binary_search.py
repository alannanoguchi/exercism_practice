def find(search_list, value):
    search_list.sort()
    left_index = 0
    right_index = len(search_list) - 1

    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        if search_list[mid_index] == value:
            return mid_index
        elif value < search_list[mid_index]:
            right_index = mid_index - 1
        elif value > search_list[mid_index]:
            left_index = mid_index + 1
    return None
