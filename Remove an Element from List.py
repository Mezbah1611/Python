
my_list = [1, 2, 3, 4, 5]


element_to_remove = 3

if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"Removed {element_to_remove} from the list.")
else:
    print(f"{element_to_remove} not found in the list.")


print("Updated list:", my_list)
