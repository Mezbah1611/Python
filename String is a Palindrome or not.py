
def is_palindrome(string):

    normalized_string = string.replace(" ", "").lower()

    return normalized_string == normalized_string[::-1]
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
