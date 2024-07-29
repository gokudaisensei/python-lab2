# main_SetOperations.py
from modules import module_SetOperations as set_ops

# Example sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Add an element
print("Add element 5 to set1:", set_ops.add_element(set1, 5))

# Remove an element
print("Remove element 2 from set1:", set_ops.remove_element(set1, 2))

# Union and Intersection
union_set, intersection_set = set_ops.union_and_intersection(set1, set2)
print("Union of set1 and set2:", union_set)
print("Intersection of set1 and set2:", intersection_set)

# Difference
print("Difference set1 - set2:", set_ops.difference(set1, set2))

# Subset check
print("Is set1 a subset of set2?", set_ops.is_subset(set1, set2))

# Length of the set
print("Length of set1:", set_ops.set_length(set1))

# Symmetric Difference
print(
    "Symmetric difference of set1 and set2:", set_ops.symmetric_difference(set1, set2)
)

# Power Set
print("Power set of set1:", set_ops.power_set(set1))

# Unique subsets
print("Unique subsets of set1:", set_ops.unique_subsets(set1))
