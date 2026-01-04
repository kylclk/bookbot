def word_counter(filepath):
    with open(filepath) as f:
        return len(f.read().split())

def character_counter(filepath):
    character_dictionary = {}
    with open(filepath) as f:
        character_list = list(f.read().lower())
    for character in character_list:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sorted_dictionary(filepath):
    def sort_on(items):
        return items["num"]

    character_dictionary = character_counter(filepath)
    dict_list = []
    for key, value in character_dictionary.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
