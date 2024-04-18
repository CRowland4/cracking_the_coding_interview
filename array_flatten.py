# Flatten an array


def flatten(array: list) -> list:
    result = []
    for item in array:
        if isinstance(item, list):
            add_elements(item, result)
        else:
            result.append(item)

    return result


def add_elements(array, current_elements: list):
    for thing in array:
        if isinstance(thing, list):
            add_elements(thing, current_elements)
        else:
            current_elements.append(thing)


def second_flatten(array: list) -> list:
    i = 0
    while True:
        if i == len(array):
            return array

        if isinstance(array[i], list):
            array = array[:i] + [*array[i]] + array[i + 1:]

        i += 1
