import numpy as np


def create_heatmap(eye_x, eye_y, eye_valid, d_time, height, width, mask_function=None):
    """
    A Function that returns a 2D numpy array representing the heat on it

    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param eye_valid:       an indexable datastructure indicating if the eye is valid (1 if yes)
    :param d_time:          the delta (in s) between each point in the eye datastructure
    :param height:          the height of the heatmap
    :param width:           the width of the heatmap
    :param mask_function:   a function that returns a mask with true where it should be active and false where it
                            should be active. The functions gets the the arguments
                            in the following order (height, width, (current_x, current_y))
    :return:                a 2D Array indicating the heat map
    """
    hmap = np.full([height, width], 0.0)
    heat = np.full([height, width], d_time)
    for idx in range(len(eye_x)):
        if eye_valid[idx] == 1:
            x_prev = eye_x[idx]
            y_prev = eye_y[idx]
            x = max(0, min(width, eye_x[idx]))
            y = max(0, min(height, eye_y[idx]))
            if x_prev != x or y_prev != y:
                continue
            mask = mask_function(height, width, (x, y))
            hmap[mask] += heat[mask]
    return hmap
