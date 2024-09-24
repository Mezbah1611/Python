
my_list = []

def append_to_list(element):
    my_list.append(element)
    print(f"Element '{element}' has been appended to the list.")

append_to_list(5)
append_to_list("Hello")
append_to_list(3.14)

print("Updated list:", my_list)
