
def list_to_string(lst, separator=' '):
    return separator.join(lst)

# Get input from the user
input_list = input("Enter the elements of the list separated by spaces: ")

elements = input_list.split()

separator = input("Enter a separator (press Enter for space): ") or ' '

result_string = list_to_string(elements, separator)

print("The converted string is:")
print(result_string)
