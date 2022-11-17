def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Jai", "age": 34},
    {"name": "Ron", "age": 30},
    {"name": "Sas", "age": 32},
]


def get_friend_name(friend):
    return friend["name"]


search(friends, "Jaidip", get_friend_name)