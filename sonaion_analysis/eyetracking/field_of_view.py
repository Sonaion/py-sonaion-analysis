import numpy as np
import sonaion_analysis.utils.masks as masks


def create_field_of_view_image(eye_x, eye_y, height, width, outer_radius, inner_radius, mask_function=None):
    """
    A Function that returns a 2D numpy array representing the heat on it

    :param eye_x:           x eye coordinates
    :param eye_y:           y eye coordinates
    :param height:          the height of the heatmap
    :param width:           the width of the heatmap
    :param outer
    _radius:    the outer radius for the field of view
    :param inner_radius:    the inner radius for the field of view
    :param mask_function:   a function that returns a mask with true where it should be active and false where it
                            should be active. The functions gets the the arguments
                            in the following order (height, width, (current_x, current_y), radius)
    :return:                a 2D Array indicating the heat map
    """
    x_prev = eye_x
    y_prev = eye_y
    x = max(0, min(width, eye_x))
    y = max(0, min(height, eye_y))
    if x_prev != x or y_prev != y:
        return np.full([height, width], 0.0)
    outer_mask = mask_function(height, width, (x, y), outer_radius)
    inner_mask = mask_function(height, width, (x, y), inner_radius)
    mask = np.logical_xor(outer_mask, inner_mask)
    return mask + 0


def create_field_of_view_video_iterator(eye_x, eye_y, eye_valid, height, width, outer_radius,
                                        inner_radius):
    """

    :param filename:            the filename for the video
    :param eye_x:               an indexable datastructure with the x eye coordinates
    :param eye_y:               an indexable datastructure with the y eye coordinates
    :param eye_valid:           an indexable datastructure indicating if the eye is valid (1 if yes)
    :param outer_radius:        outer radius for the field of view
    :param inner_radius:        inner radius for the field of view
    :return:                    yields the masks for the discrete time points
    """
    for idx in range(len(eye_x)):
        if eye_valid[idx] == 1:
            mask_function = masks.create_circular_mask
            mask = create_field_of_view_image(eye_x[idx], eye_y[idx], height, width, outer_radius, inner_radius, mask_function)
            yield mask
        else:
            yield np.full([height, width], 0.0)
