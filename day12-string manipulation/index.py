def reverse_string(string):
    return string[::-1]

def count_occurrences(string, char):
    return string.count(char)

def is_palindrome(string):
    return string == string[::-1]

user_input = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)

# Count occurrences of a specific character
char_to_count = input("Enter a character to count: ")
occurrences = count_occurrences(user_input, char_to_count)
print("Occurrences of", char_to_count + ":", occurrences)

# Check if the string is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
