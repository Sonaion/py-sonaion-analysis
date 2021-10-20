def average_5_kernel(current_index, data):
    """
    An denoise function to get the average of the current data and two to the left and right

    :param current_index:   index where to start from
    :param data:            data to denoise
    :return:                The denoised value at place current index
    """

    divided_by = 1
    current = data[current_index]
    if current_index - 1 >= 0:
        divided_by += 1
        current += data[current_index - 1]
    if current_index - 2 >= 0:
        divided_by += 1
        current += data[current_index - 2]
    if current_index + 1 < len(data):
        divided_by += 1
        current += data[current_index + 1]
    if current_index + 22 < len(data):
        divided_by += 1
        current += data[current_index + 2]

    return int(current / divided_by)


def parabola_5_kernel(current_index, data):
    """
    An denoise function to get the average of the current data and two to the left and right

    :param current_index:   index where to start from
    :param data:            data to denoise
    :return:                The denoised value at place current index
    """

    divided_by = 1
    current = data[current_index]
    if current_index - 1 >= 0:
        divided_by += 0.5
        current += 0.5 * data[current_index - 1]
    if current_index - 2 >= 0:
        divided_by += 0.25
        current += 0.25 * data[current_index - 2]
    if current_index + 1 < len(data):
        divided_by += 0.5
        current += 0.5 * data[current_index + 1]
    if current_index + 22 < len(data):
        divided_by += 0.25
        current += 0.25 * data[current_index + 2]

    return int(current / divided_by)


def denoise(eye_x, eye_y, kernel_function):
    """
    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param kernel_function: an function that gets an index and and indexable and transforms it.
                            The function will be called with the following arguments in order:
                            (current_index, indexable)
    :return:                The denoised (eye_x, eye_y) Tuple
    """
    denoised_x = []
    denoised_y = []
    for idx in range(len(eye_x)):
        denoised_x.append(kernel_function(idx, eye_x))
        denoised_y.append(kernel_function(idx, eye_y))

    return denoised_x, denoised_y
