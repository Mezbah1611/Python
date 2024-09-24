s
def add_lists(list1, list2):

    if len(list1) != len(list2):
        print("Both lists must have the same length.")
        return []


    result = [a + b for a, b in zip(list1, list2)]
    return result
list_a = [1, 2, 3]
list_b = [4, 5, 6]

result_list = add_lists(list_a, list_b)
print("Resultant list:", result_list)
