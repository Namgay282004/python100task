# Write a function called "is_sorted" that takes a list of numbers as an argument and returns True if the list is sorted in ascending order, False otherwise.

def is_sorted(num_list):
    # Check if the list is sorted in ascending order
    return all(num_list[i] <= num_list[i + 1] for i in range(len(num_list) - 1))

# Example :
numbers = [1, 2, 3, 4, 5]
print(is_sorted(numbers))  


