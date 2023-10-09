def check_duplicates(input_list):
    duplicates = set()
    seen = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    if duplicates:
        return duplicates
    else:
        return "no duplicates"


fruits = ['orange', 'banana', 'grape', 'apple']
print(check_duplicates(fruits))

# names = ['Yoda', 'Moses', 'Joshua', 'Mark']
# print(check_duplicates(names))
