def copy(obj, deep_copy=True):
    """
    A function that allows the use of deep coping or shallow coping a value.

    :param obj:         value to copy.
    :param deep_copy:   flag that indicated if a deep copy should be done.
    :return:            return a copy of the object.
    """
    if deep_copy:
        return obj.copy()
    return obj


def get_standard(obj, standard):
    """
    A function that allows to return a standard value for an object, if the object is None.

    :param obj:         Object to check if it's None.
    :param standard:    Standard value for the object
    :return:            return the object or the standard value
    """
    if obj is None:
        return standard
    return obj


def get_from(indexable, idx):
    if indexable is None or len(indexable) >= idx:
        return None
    return indexable[idx]
