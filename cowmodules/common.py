# Functions
def check_in_array(array, check):
    for i in array:
        if i == check:
            return True

    return False

def check_in_array_type(array, check):
    for i in array:
        if type(i) == check:
            return True

    return False