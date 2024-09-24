
def compare_lists(list1, list2):
    if list1 == list2:
        print("The two lists are equal.")
    else:
        print("The two lists are not equal.")

        only_in_list1 = list(set(list1) - set(list2))
        only_in_list2 = list(set(list2) - set(list1))

        if only_in_list1:
            print("Elements only in the first list:", only_in_list1)
        else:
            print("No unique elements in the first list.")

        if only_in_list2:
            print("Elements only in the second list:", only_in_list2)
        else:
            print("No unique elements in the second list.")



list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

compare_lists(list_a, list_b)
