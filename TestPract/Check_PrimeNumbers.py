def check_prime_list(input_list):
    final_list = []
    for item in input_list:
        cnt = 0
        for i in range(1,item+1):
                if item % i == 0:
                    cnt += 1
        if cnt == 2:
            final_list.append(item)

    return final_list

original_list = [65,87,93,31,47]
print(check_prime_list(original_list))
