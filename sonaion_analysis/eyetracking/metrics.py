import math


def classify_saccades(eye_x, eye_y, d_time, treshhold):
    """
    a function that classifies sacades based on a threshhold in pixel per second

    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param d_time:          the delta time between each eye record
    :param treshhold:       the threshhold in pixel per second
    :return:                a list with values which indicate if the move from the previos is a saccade.
                            First value will ever be 0 because there is no previos value for the velcoity.
                            Saccades are indicated by a 1 and otherwise it is 0.
    """

    saccades = [0]
    prev_x = eye_x[0]
    prev_y = eye_y[0]
    for idx in range(1, len(eye_x)):
        current_x = eye_x[1]
        current_y = eye_y[1]
        distance = math.sqrt(math.pow(current_x - prev_x, 2.0) + math.pow(current_y - prev_y, 2.0))
        velocity = distance / d_time
        if velocity < treshhold:
            saccades.append(0)
        else:
            saccades.append(1)
    return saccades


def count_saccades(saccades):
    """
    A Function that counts the number of distinct saccades

    :param saccades:    a list with values which indicate if the move from the previos is a saccade.
    :return:            a number of indicating the amount of different saccades
    """
    saccade_count = 0
    is_currently = False
    for value in saccades:
        if value == 1 and is_currently == False:
            saccade_count +=1
            is_currently = True
        if value == 0 and is_currently == True:
            is_currently = False
    return saccade_count

def time_of_saccades(saccades, d_time):
    """
    A Function to get the start and end time of the individual saccades

    :param saccades:    a list with values which indicate if the move from the previos is a saccade.
    :param d_time:      the delta time in seconds between each step
    :return:            return a list of tuples with (start_time_inclusive, end_time_exclusive)
    """
    saccade_times = []
    is_currently = False
    current_time = 0.0
    current_start_time = None
    for value in saccades:
        if value == 1 and is_currently == False:
            current_start_time = current_time
            is_currently = True
        if value == 0 and is_currently == True:
            is_currently = False
            saccade_times.append((current_start_time, current_time))
        current_time += d_time
    return saccade_times

def average_saccades_time(saccades_times):
    """

    :param saccades_times:  a list of tuples with (start_time_inclusive, end_time_exclusive)
    :return:                returns the average time of saccades
    """

    return sum([saccade_time[1]-saccade_time[0] for saccade_time in saccades_times])/len(saccades_times)


def classify_fixxation(eye_x, eye_y, d_time, treshhold):
    """
    a function that classifies fixxations based on a threshhold in pixel per second

    :param eye_x:           an indexable datastructure with the x eye coordinates
    :param eye_y:           an indexable datastructure with the y eye coordinates
    :param d_time:          the delta time between each eye record
    :param treshhold:       the threshhold in pixel per second
    :return:                a list with values which indicate if the move from the previos is a fixxations.
                            First value will ever be 0 because there is no previos value for the velcoity.
                            Fixxations are indicated by a 1 and otherwise it is 0.
    """

    fixxations = [0]
    prev_x = eye_x[0]
    prev_y = eye_y[0]
    for idx in range(1, len(eye_x)):
        current_x = eye_x[1]
        current_y = eye_y[1]
        distance = math.sqrt(math.pow(current_x - prev_x, 2.0) + math.pow(current_y - prev_y, 2.0))
        velocity = distance / d_time
        if velocity >= treshhold:
            fixxations.append(0)
        else:
            fixxations.append(1)
    return fixxations

def count_fixxations(fixxations):
    """
    A Function that counts the number of distinct fixxations

    :param fixxations:  a list with values which indicate if the move from the previos is a fixxations.
    :return:            a number of indicating the amount of different fixxations
    """
    fixxations_count = 0
    is_currently = False
    for value in fixxations:
        if value == 1 and is_currently == False:
            fixxations_count +=1
            is_currently = True
        if value == 0 and is_currently == True:
            is_currently = False
    return fixxations_count

def time_of_fixxations(fixxations, d_time):
    """
    A Function to get the start and end time of the individual fixxations

    :param fixxations:    a list with values which indicate if the move from the previos is a fixxation.
    :param d_time:      the delta time in seconds between each step
    :return:            return a list of tuples with (start_time_inclusive, end_time_exclusive)
    """
    fixxation_times = []
    is_currently = False
    current_time = 0.0
    current_start_time = None
    for value in fixxations:
        if value == 1 and is_currently == False:
            current_start_time = current_time
            is_currently = True
        if value == 0 and is_currently == True:
            is_currently = False
            fixxation_times.append((current_start_time, current_time))
        current_time += d_time
    return fixxation_times


def average_fixxations_time(fixxations_times):
    """

    :param fixxations_times:  a list of tuples with (start_time_inclusive, end_time_exclusive)
    :return:                returns the average time of fixxations
    """

    return sum([fixxation_time[1] - fixxation_time[0] for fixxation_time in fixxations_times]) / len(fixxations_times)