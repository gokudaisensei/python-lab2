from modules.module_DictionaryOperations import (
    merging_Dict,
    common_keys,
    invert_dict,
    common_key_value_pairs,
)

# Define example dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 5, "d": 6}
dict3 = {"a": 1, "c": 3, "e": 7}

# Merging dictionaries
merged = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# Finding common keys
common_keys_result = common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)

# Inverting a dictionary
inverted_dict1 = invert_dict(dict1)
print("Inverted Dictionary:", inverted_dict1)

# Finding common key-value pairs
common_kv_pairs = common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_kv_pairs)
