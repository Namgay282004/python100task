# Write a function called "find_longest_word" that takes a string as an argument and returns the longest word in the string.
# Assume that words in the string are separated by spaces, and there are no punctuation marks.

def find_longest_word(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize variables to store the longest word and its length
    longest_word = ""
    max_length = 0

    # Iterate through the words to find the longest one
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word

# Example usage:
input_string = "i enjoy coding!!"
result = find_longest_word(input_string)
print(result)  # Output: "jumped"
