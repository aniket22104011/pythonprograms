def duplicate(int_list):
    count_dict = {}
    for number in int_list:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    duplicates = [number for number, count in count_dict.items() if count > 1]
    
    return duplicates

numbers = [4, 5, 6, 7, 4, 8, 9, 5, 1, 2]
print("Duplicates in the list:", duplicate(numbers))
