import copy


def compare_dict_copies(original_dict):
    shallow_copy = original_dict.copy()
    deep_copy = copy.deepcopy(original_dict)

    # Modify original dictionary
    original_dict['new_key'] = 'new_value'

    # Append to list values, if any
    for key, value in original_dict.items():
        if isinstance(value, list):
            value.append('new_item')

    return (original_dict, shallow_copy, deep_copy)


# Example usage:
original = {
    'a': 1,
    'b': [2, 3],
    'c': {'d': 4}
}

modified_original, shallow_copy, deep_copy = compare_dict_copies(original)

print("Modified Original:", modified_original)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)


