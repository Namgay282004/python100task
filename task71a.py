# Write a function called "find_common_elements" that takes two lists as arguments and returns a new list containing the common elements between the two input lists.

# Example:
# find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # Should print [3, 4, 5]

def find_common_element(list1, list2):
    return list(set(list1) & set(list2))
print(find_common_element([1,2,3,4],[2,3,4,5,6]))