def split_list_at_third_element(input_list):
    output = [[] for _ in range(3)]

    for index, item in enumerate(input_list):
        output[index % 3].append(item)
    return output


sample_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'I', 'j', 'k', 'l', 'm', 'n']
output = split_list_at_third_element(sample_input)
print(output)
