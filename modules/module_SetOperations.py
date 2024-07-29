from typing import Set, List, Tuple

def add_element(s: Set, element: any) -> Set:
    """Add an element to a set, ensuring no errors if the element is already present."""
    s.add(element)
    return s


def remove_element(s: Set, element: any) -> Set:
    """Remove an element from a set, ensuring no errors if the element is not present."""
    s.discard(element)  # discard does not raise an error if the element is not found
    return s


def union_and_intersection(s1: Set, s2: Set) -> Tuple[Set, Set]:
    """Return the union and intersection of two sets, handling empty sets correctly."""
    union_set = s1.union(s2)
    intersection_set = s1.intersection(s2)
    return union_set, intersection_set


def difference(s1: Set, s2: Set) -> Set:
    """Return the difference S1−S2, handling empty sets correctly."""
    return s1.difference(s2)


def is_subset(s1: Set, s2: Set) -> bool:
    """Check if set S1 is a subset of set S2, handling empty sets correctly."""
    return s1.issubset(s2)


def set_length(s: Set) -> int:
    """Find the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count


def symmetric_difference(s1: Set, s2: Set) -> Set:
    """Compute the symmetric difference of two sets."""
    return s1.symmetric_difference(s2)


def power_set(s: Set) -> List[List[any]]:
    """Compute the power set of a given set."""
    power_set = [[]]
    for element in s:
        subsets = [subset + [element] for subset in power_set]
        power_set.extend(subsets)
    return power_set


def unique_subsets(s: Set) -> Set[frozenset]:
    """Get all unique subsets of a given set."""
    return set(frozenset(subset) for subset in power_set(s))
