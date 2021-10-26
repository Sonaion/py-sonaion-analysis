from sonaion_analysis.utils.smallestenclosingcircle import make_circle


def create_fixxation_map(eye_x, eye_y, fixxation_classifier):
    """
    :param eye_x:                   an indexable datastructure with the x eye coordinates
    :param eye_y:                   an indexable datastructure with the y eye coordinates
    :param fixxation_classifier:    a list with values which indicate if the move from the previos is a fixxations.
    :return:                        a List of circles which bound around the fixxation and witch saccades they dont bound.
                                    The List is organized Liked this [((circle1_x, circle1_y), circle1_radius), ...])
    """

    # process into fixxation and saccade movements
    points_array = []
    currently_fixxation = False
    current_points = []

    for idx, classifier in enumerate(fixxation_classifier):
        if classifier == 1 and currently_fixxation == False:
            current_points = [(eye_x[idx], eye_y[idx])]
        elif classifier == 1:
            current_points.append((eye_x[idx], eye_y[idx]))
        elif classifier == 0 and currently_fixxation == True:
            points_array.append((current_points.copy(), True))
            current_points = []
            currently_fixxation = False
            points_array.append(([(eye_x[idx], eye_y[idx])], False))
        else:
            points_array.append(([(eye_x[idx], eye_y[idx])], True))

    circles = [(make_circle(points), is_fixxation) for points, is_fixxation in points_array]
    circles = [((x, y), radius, is_fixxation) for (x, y, radius, is_fixxation) in circles]

    return circles
