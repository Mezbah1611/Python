
def count_occurrences(main_string, substring):
    return main_string.count(substring)

main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

occurrences = count_occurrences(main_string, substring)
print(f'The substring "{substring}" occurs {occurrences} times in the main string.')
