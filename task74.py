# Write a function called "reverse_words" that takes a string as an argument and returns a string where the words are reversed.
# For example, "Hello, world!" should become "olleH, dlrow!".

def reverse_words(input_string):
    # Split the input string into words
    words = input_string.split()

    # Reverse each word and rebuild the string
    reversed_words = [word[::-1] for word in words]
    reversed_string = " ".join(reversed_words)
    return reversed_string

# Example usage:
input_string = "Hello world!"
result = reverse_words(input_string)
print(result)  # Output: "olleH, dlrow!"
