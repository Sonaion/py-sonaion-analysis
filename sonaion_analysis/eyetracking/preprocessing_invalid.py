def remove_invalid(eye_x, eye_y, pupil_diameter, eye_valid):
    """
    A Function to remove invalid eye data, careful there is no machanism to synchronise left and right eye afterwards

    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param pupil_diameter:  an indexable datastructure with the pupil diameter
    :param eye_valid:       an indexable datastructure indicating if the eye is valid (1 if yes)
    :return                 a tuple (eye_x, eye_y, pupil_diameter, eye_valid)
    """

    x = []
    y = []
    pupil = []
    valid = []

    for idx, value in enumerate(eye_valid):
        if value == 1:
            x.append(eye_x[idx])
            y.append(eye_y[idx])
            pupil.append(pupil_diameter[idx])
            valid.append(1)

    return x, y, pupil, valid


def replace_with_prev_invalid(eye_x, eye_y, pupil_diameter, eye_valid):
    """
    A Function to remove invalid eye data, careful there is no machanism to synchronise left and right eye afterwards

    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param pupil_diameter:  an indexable datastructure with the pupil diameter
    :param eye_valid:       an indexable datastructure indicating if the eye is valid (1 if yes)
    :return                 a tuple (eye_x, eye_y, pupil_diameter, eye_valid)
    """

    prev_x = None
    prev_y = None
    prev_pupil = None
    for idx, value in enumerate(eye_valid):
        if value == 1:
            prev_x = eye_x[idx]
            prev_y = eye_y[idx]
            prev_pupil = pupil_diameter[idx]
            break

    x = []
    y = []
    pupil = []
    valid = []

    for idx, value in enumerate(eye_valid):
        if value == 1:
            x.append(eye_x[idx])
            y.append(eye_y[idx])
            pupil.append(pupil_diameter[idx])
            prev_x = eye_x[idx]
            prev_y = eye_y[idx]
            prev_pupil = pupil_diameter[idx]
        else:
            x.append(prev_x)
            y.append(prev_y)
            pupil.append(prev_pupil)
        valid.append(1)

    return x, y, pupil, valid
