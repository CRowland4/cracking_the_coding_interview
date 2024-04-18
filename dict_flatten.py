def dict_flatten(dictionary: dict) -> dict:
    pairs = []
    keys_to_delete = []

    for key, value in dictionary.items():
        if isinstance(value, dict):
            add_pairs(value, pairs)
            keys_to_delete.append(key)

    for pair in pairs:
        dictionary[pair[0]] = pair[1]

    for key in keys_to_delete:
        del dictionary[key]

    return dictionary


def add_pairs(dictionary: dict, pairs: list):
    for key, val in dictionary.items():
        if isinstance(val, dict):
            add_pairs(val, pairs)
        else:
            pairs.append((key, val))
