
def list_to_string(lst):

    return ' '.join(lst)

input_list = input("Enter the elements of the list separated by spaces: ")

elements = input_list.split()

result_string = list_to_string(elements)
print("The converted string is:")
print(result_string)
