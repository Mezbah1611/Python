import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
input_string = input("Enter a string: ")
result_string = remove_punctuation(input_string)
print("String without punctuation:")
print(result_string)
