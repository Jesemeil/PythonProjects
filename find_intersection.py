def find_intersection(list1, list2):
    intersection = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in intersection:
                intersection.append(item1)
    return tuple(intersection)


list_1 = [20, 30, 30, 60, 65, 75, 80, 85]
list_2 = [42, 30, 80, 80, 65, 68, 88, 95]

intersection_tuple = find_intersection(list_1, list_2)
print("Intersection:", intersection_tuple)
