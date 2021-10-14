import numpy as np


def create_sequence_diagram_y(eye_y, eye_valid, height, width, offset=0, step=0.5, should_skip=True):
    """
    A Function that returns a 2D numpy array representing the sequence diagram on it

    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param eye_valid:       an indexable datastructure indicating if the eye is valid (1 if yes)
    :param height:          the height of the heatmap
    :param width:           the width of the heatmap
    :param offset:          the offset from the top, to where to start the sequence diagram in pixel
    :param step:            the step from the top in pixel
    :param should_skip:     Indicates if the step should be taken when the eye is invalid
    :return:                a 2D Array indicating the sequence diagramm
    """
    sequence = np.full([height, width], 0.0)
    current_x = offset
    current = None
    x_step = step

    for idx, y in enumerate(eye_y):
        if eye_valid[idx] == 1:
            current = (min(max(0, y), height - 1), min(max(0, current_x), width - 1))
            break

    for idx, y in enumerate(eye_y):
        old_x = current[1]
        old_y = current[0]
        next_y = min(max(0, y), height - 1)
        next_x = min(max(0, current[1] + x_step), width - 1)
        if eye_valid[idx] == 1:
            sequence[old_y, int(old_x): int(next_x)] = 1.0
            sequence[old_y:next_y, int(next_x)] = 1.0
            sequence[next_y:old_y, int(next_x)] = 1.0
        if eye_valid[idx] == 1 or not should_skip:
            current = (next_y, next_x)

    return sequence

def create_classified_sequence_diagram_y(eye_y, eye_classification, height, width, offset=0, step=0.5):
    """
    A Function that returns a 2D numpy array representing the sequence diagram on it

    :param eye_y:                   an indexable datastructure with the y eye coordinates
    :param eye_classification:      an indexable datastructure indicating a classification of
                                    the eyemovement (e.g. invalid=1, fixxation=2 or saccade=3)
    :param height:                  the height of the heatmap
    :param width:                   the width of the heatmap
    :param offset:                  the offset from the top, to where to start the sequence diagram in pixel
    :param step:                    the step from the top in pixel
    :return:                        a 2D Array indicating the sequence diagramm
    """
    sequence = np.full([height, width], 0.0)
    current_x = offset
    current = None
    x_step = step

    for idx, y in enumerate(eye_y):
        current = (min(max(0, y), height - 1), min(max(0, current_x), width - 1))
        break

    for idx, y in enumerate(eye_y):
        old_x = current[1]
        old_y = current[0]
        next_y = min(max(0, y), height - 1)
        next_x = min(max(0, current[1] + x_step), width - 1)
        sequence[old_y, int(old_x): int(next_x)] = eye_classification[idx]
        sequence[old_y:next_y, int(next_x)] = eye_classification[idx]
        sequence[next_y:old_y, int(next_x)] = eye_classification[idx]
        current = (next_y, next_x)

    return sequence


def create_sequence_diagram_x(eye_x, eye_valid, height, width, offset=0, step=0.5, should_skip=True):
    """
    A Function that returns a 2D numpy array representing the sequence diagram on it

    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_valid:       an indexable datastructure indicating if the eye is valid (1 if yes)
    :param height:          the height of the heatmap
    :param width:           the width of the heatmap
    :param offset:          the offset from the top, to where to start the sequence diagram in pixel
    :param step:            the step from the top in pixel
    :param should_skip:     Indicates if the step should be taken when the eye is invalid
    :return:                a 2D Array indicating the sequence diagramm
    """
    sequence = np.full([height, width], 0.0)
    current_y = offset
    current = None
    y_step = step

    for idx, x in enumerate(eye_x):
        if eye_valid[idx] == 1:
            current = (min(max(0, current_y), height - 1), min(max(0, x), width - 1))
            break

    for idx, x in enumerate(eye_x):
        if eye_valid[idx] == 1:
            old_x = current[1]
            old_y = current[0]
            next_y = min(max(0, current[0] + y_step), height - 1)
            next_x = min(max(0, x), width - 1)

            if eye_valid[idx] == 1:
                sequence[int(old_y): int(next_y), old_x] = 1.0
                sequence[int(next_y), old_x:next_x] = 1.0
                sequence[int(next_y), next_x:old_x] = 1.0
            if eye_valid[idx] == 1 or not should_skip:
                current = (next_y, next_x)

    return sequence

def create_classified_sequence_diagram_x(eye_x, eye_classification, height, width, offset=0, step=0.5):
    """
    A Function that returns a 2D numpy array representing the sequence diagram on it

    :param eye_x:                   an indexable datastructure with the x eye coordinates
    :param eye_classification:      an indexable datastructure indicating a classification of
                                    the eyemovement (e.g. invalid=1, fixxation=2 or saccade=3)
    :param height:                  the height of the heatmap
    :param width:                   the width of the heatmap
    :param offset:                  the offset from the top, to where to start the sequence diagram in pixel
    :param step:                    the step from the top in pixel
    :return:                        a 2D Array indicating the sequence diagramm
    """
    sequence = np.full([height, width], 0.0)
    current_y = offset
    current = None
    y_step = step

    for idx, x in enumerate(eye_x):
        current = (min(max(0, current_y), height - 1), min(max(0, x), width - 1))
        break

    for idx, x in enumerate(eye_x):
            old_x = current[1]
            old_y = current[0]
            next_y = min(max(0, current[0] + y_step), height - 1)
            next_x = min(max(0, x), width - 1)

            sequence[int(old_y): int(next_y), old_x] = eye_classification[idx]
            sequence[int(next_y), old_x:next_x] = eye_classification[idx]
            sequence[int(next_y), next_x:old_x] = eye_classification[idx]
            current = (next_y, next_x)

    return sequence
