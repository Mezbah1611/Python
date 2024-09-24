
def concatenate_strings(str1, str2, separator=''):
    return str1 + separator + str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

separator = input("Enter a separator (press Enter for no separator): ") or ''

result_string = concatenate_strings(string1, string2, separator)

print("The concatenated string is:")
print(result_string)
