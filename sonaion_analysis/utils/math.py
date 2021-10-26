def clamp(value, min_value, max_value):
    """
    Clamp The given value between a min and a max value.

    :param value:       Value to be clamped
    :param min_value:   min value to clamp against
    :param max_value:   max value to clamp against
    :return:            clamped value
    """
    if value < min_value:
        return min_value
    elif value > max_value:
        return max
    return value
