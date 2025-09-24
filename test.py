def repeated_values(input_list):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
repeated_values = find_repeated_values_set(my_list)
print("Repeated values: {repeated_values}")
