import string
from collections import Counter

def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            text = file.read()

            # Word count
            word_count = len(text.split())

            # Character count
            character_count = len(text)

            # Remove punctuation and convert text to lowercase
            text = text.translate(str.maketrans('', '', string.punctuation)).lower()

            # Count the occurrences of each word
            word_frequency = Counter(text.split())

            # Most common words
            num_most_common = 5  # Change this value to display more or fewer common words
            most_common_words = word_frequency.most_common(num_most_common)

            # Display the results
            print(f"Word count: {word_count}")
            print(f"Character count: {character_count}")
            print(f"Most common words:")
            for word, count in most_common_words:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


# Example usage
file_path = 'sample.txt'
analyze_text(file_path)
