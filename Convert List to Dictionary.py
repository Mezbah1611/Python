
def list_to_dict(input_list):

    if len(input_list) % 2 != 0:
        print("The list must contain pairs of elements.")
        return {}
    result_dict = {}
    for i in range(0, len(input_list), 2):
        key = input_list[i]
        value = input_list[i + 1]
        result_dict[key] = value

    return result_dict
example_list = ['a', 1, 'b', 2, 'c', 3]
converted_dict = list_to_dict(example_list)

print("Converted Dictionary:", converted_dict)
