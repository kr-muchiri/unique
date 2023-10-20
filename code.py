def unique_elements(words_list):
    """Return the number of unique words in a list."""
    unique_words = set()

    for word in words_list:
        if word.isalpha():  # Check if the word contains only alphabetic characters
            unique_words.add(word.lower())  # Convert word to lowercase and add to the set

    return len(unique_words)


def main():
    # Ask the user for the name of the file
    filename = input("Enter the name of the file: ")

    # Open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Split the file content into words
    words = content.split()

    # Count the number of words
    total_words = sum(1 for word in words if word.isalpha())

    # Report the results
    print(f"Number of words in the file: {total_words}")
    print(f"Number of unique words in the file: {unique_elements(words)}")

if __name__ == "__main__":
    main()
