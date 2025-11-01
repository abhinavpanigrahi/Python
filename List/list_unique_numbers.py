
def unique_numbers(input_list):
    result_list = []
    for item in input_list:
        if item not in result_list:
            result_list.append(item)
    return result_list

list1 = [1, 2, 3, 1, 4, 5, 5, 7, 7, 0, 1, 'abc', 'abc']
print(f"Unique List : {unique_numbers(list1)}")

