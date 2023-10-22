# Write a function called "multiply_lists" that takes two lists of equal length as arguments and returns a new list where each element is the product of the corresponding elements from the input lists.
# Example:
# List1 = [1,2,3]
# List2 = [4,5,6]
# multiply_lists(List1, List2))  Should print [4, 10, 18]

def multiply_lists(list1, list2):
    return [a *b for a, b in zip(list1,list2)]
#  Example:

print(multiply_lists([1,2,3],[4,5,6]))




