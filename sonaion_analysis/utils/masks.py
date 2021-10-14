import numpy as np


def create_circular_mask(height, width, center=None, radius=None):
    """
    A Function to return a 2D numpy array with a circluar mask.

    :param height:  Height in pixel for the mask
    :param width:   Width in pixel for the mask
    :param center:  (x,y) Tuple with pixel coordinates of the mask
    :param radius:  radius in pixel of the circle
    :return:        2D Numpy Array where ones represents the circle and zeros everything else
    """

    # use the middle of the image for the center if none is given
    if center is None:
        center = (int(width / 2), int(height / 2))
    # use the smallest distance between the center and image walls
    if radius is None:
        radius = min(center[0], center[1], width - center[0], height - center[1])

    Y, X = np.ogrid[:height, :width]
    x_low = max(center[0] - radius, 0.0)
    x_high = min(center[0] + radius, width)
    y_low = max(center[1] - radius, 0.0)
    y_high = min(center[1] + radius, width)
    X = X[:, x_low:x_high]
    Y = Y[y_low:y_high]
    dist_from_center = np.full([height, width], radius + 1)
    dist_from_center[y_low:y_high, x_low:x_high] = np.sqrt((X - center[0]) ** 2 + (Y - center[1]) ** 2)

    mask = dist_from_center <= radius
    return mask


def create_rectangular_mask(height, width, center=None, dimension=None):
    """
    A Function to return a 2D numpy array with a circluar mask.

    :param height:      Height in pixel for the mask
    :param width:       Width in pixel for the mask
    :param center:      (x,y) Tuple with pixel coordinates of the mask
    :param dimension:   (rectangle_width, rectangle_height) Tuple in pixel units
    :return:            2D Numpy Array where ones represents the circle and zeros everything else
    """

    # use the middle of the image for the center if none is given
    if center is None:
        center = (int(width / 2), int(height / 2))
    # use the smallest distance between the center and image walls
    if dimension is None:
        dimension = (int(width / 2), int(height / 2))

    lower_y = max(0, center[1] - int(dimension[1] / 2))
    upper_y = min(height, center[1] + int(dimension[1] / 2) + 1)

    lower_x = max(0, center[0] - int(dimension[0] / 2))
    upper_x = min(width, center[0] + int(dimension[0] / 2) + 1)

    mask = np.full([height, width], False)
    mask[lower_y:upper_y, lower_x:upper_x] = True
    return mask
