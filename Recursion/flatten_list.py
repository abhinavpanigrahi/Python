def flatten_list(numList):
    flat = []
    for num in numList:
        if isinstance(num, list):
            flat.extend(flatten_list(num))
        else:
            flat.append(num)
    return flat

data = [1, [2, [3, 4], 5], 6]
print(flatten_list(data))