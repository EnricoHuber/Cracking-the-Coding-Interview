"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
"""
def check_dups(list):
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    return new_list


list_input = [1, 2, 3, 4, 5, 6, 2, 4, 3, 3, 3]
print(check_dups(list_input))
