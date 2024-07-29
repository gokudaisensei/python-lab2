def merging_Dict(*args):
    """Merges multiple dictionaries into one."""
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict


def common_keys(*args):
    """Finds common keys in multiple dictionaries."""
    if not args:
        return set()

    common_keys_set = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys_set.intersection_update(dictionary.keys())

    return common_keys_set


def invert_dict(dictionary):
    """Inverts a dictionary, swapping keys and values. If multiple keys have the same value, groups these keys in a list."""
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
    return inverted_dict


def common_key_value_pairs(*args):
    """Finds common key-value pairs across multiple dictionaries."""
    if not args:
        return {}

    common_pairs = {k: v for k, v in args[0].items()}
    for dictionary in args[1:]:
        common_pairs = {
            k: v
            for k, v in common_pairs.items()
            if k in dictionary and dictionary[k] == v
        }

    return common_pairs
