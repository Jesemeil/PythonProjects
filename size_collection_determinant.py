def collection_size(collection):
    count = 0
    for _ in collection:
        count += 1
    return count


my_list = [1, 2, 3, 4, 5]
print(collection_size(my_list))

my_tuple = (1, 2, 3)
print(collection_size(my_tuple))

my_set = {1, 2, 3, 4}
print(collection_size(my_set))

my_string = "Hello, World!"
print(collection_size(my_string))
