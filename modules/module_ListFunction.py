# module_ListFunction.py


def find_maximum(values):
    """Find the maximum value in a given list."""
    if not values:
        return None
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
    return max_value


def find_minimum(values):
    """Find the minimum value in a given list."""
    if not values:
        return None
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value


def calculate_sum(values):
    """Calculate the sum of all elements in a list."""
    total = 0
    for value in values:
        total += value
    return total


def compute_average(values):
    """Compute the average of the list."""
    if not values:
        return None
    total = calculate_sum(values)
    return total / len(values)


def determine_median(values):
    """Determine the median of a list."""
    if not values:
        return None
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_values[mid - 1] + sorted_values[mid]) * 0.5
    else:
        median = sorted_values[mid]
    return median
