def count_names_starting_with_S(names):
    names_dict = {}

    for name in names:
        if name.startswith("S") or name.startswith("s"):
            capitalized_name = name.capitalize()
            if capitalized_name in names_dict:
                names_dict[capitalized_name] += 1
            else:
                names_dict[capitalized_name] = 1

    return names_dict


print(count_names_starting_with_S(
    ["Joe", "Daniel", "Seyi", "Kelvin", "Muhammad", "Hakimi", "segun", "Ashley", "seyi", "samuel","Segun"]))



