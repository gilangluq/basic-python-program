def sort_words(sentence):
    """Function to sort words in a sentence alphabetically."""
    # Split the sentence into words
    words = sentence.split()
    # Sort the words alphabetically
    sorted_words = sorted(words, key=str.lower)  # Case-insensitive sort
    return sorted_words

# Prompt user for input
sentence = input("Enter a sentence: ")

# Sort the words and display the result
sorted_list = sort_words(sentence)
print("Words in alphabetical order:")
print(" ".join(sorted_list))
