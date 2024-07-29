# main_ListOperations.py
from modules import module_ListFunction
from random import randint

# Creating lists using list comprehensions
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
squares = [x**2 for x in range(1, 11)]
random_values = [randint(1, 100) for _ in range(10)]

# Demonstrating the use of module functions with these lists

# Even numbers list
print("Even Numbers:", even_numbers)
print("Maximum:", module_ListFunction.find_maximum(even_numbers))
print("Minimum:", module_ListFunction.find_minimum(even_numbers))
print("Sum:", module_ListFunction.calculate_sum(even_numbers))
print("Average:", module_ListFunction.compute_average(even_numbers))
print("Median:", module_ListFunction.determine_median(even_numbers))
print()

# Odd numbers list
print("Odd Numbers:", odd_numbers)
print("Maximum:", module_ListFunction.find_maximum(odd_numbers))
print("Minimum:", module_ListFunction.find_minimum(odd_numbers))
print("Sum:", module_ListFunction.calculate_sum(odd_numbers))
print("Average:", module_ListFunction.compute_average(odd_numbers))
print("Median:", module_ListFunction.determine_median(odd_numbers))
print()

# Squares list
print("Squares:", squares)
print("Maximum:", module_ListFunction.find_maximum(squares))
print("Minimum:", module_ListFunction.find_minimum(squares))
print("Sum:", module_ListFunction.calculate_sum(squares))
print("Average:", module_ListFunction.compute_average(squares))
print("Median:", module_ListFunction.determine_median(squares))
print()

# Random values list
print("Random Values:", random_values)
print("Maximum:", module_ListFunction.find_maximum(random_values))
print("Minimum:", module_ListFunction.find_minimum(random_values))
print("Sum:", module_ListFunction.calculate_sum(random_values))
print("Average:", module_ListFunction.compute_average(random_values))
print("Median:", module_ListFunction.determine_median(random_values))
print()
