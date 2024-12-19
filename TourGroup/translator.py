SEPARATOR = "\n========================="

def get_key_value_tupel():
    update = ""
    while update.count(",") != 1:
        update = input("\nPlease insert a word and the corresponding translation,comma separated (german,english): ")
    split = update.split(",")
    key = split[0].strip()
    value = split[1].strip()
    return key, value

def get_mode(modes):
    print("\nModes:")
    for mode in modes:
        print("\t", mode + ":", modes.get(mode))
    return input("please insert a mode: ")

def print_dictionary(dict: dict):
    print("\nDictionary entries (DE -> EN):")
    for key, value in dict.items():
        print(f"\t{key} -> {value}")

def translate(dict: dict):
    german = input("\nPlease insert a word you wish to translate: ")
    if german in dict:
        print(f"{german} -> {dict.get(german)}")
    else:
        print(f"No translation for {german}")

def add_entry_to_dictionary(dict: dict):
    key, value = get_key_value_tupel()
    if key in dict:
        print(f"Can not add entry, key '{key}' is already present in dictionary.")
        return
    dict.update({key: value})
    print(f"Added translation: {key} -> {dict.get(key)}.")

def update_entry_in_dictionary(dict: dict):
    key, value = get_key_value_tupel()
    if key not in dict:
        print(f"Not able to update entry with key '{key}', key not existing.")
        return
    dict.update({key: value})
    print(f"Updated translation: {key} -> {dict.get(key)}.")

def remove_entry_from_dictionary(dict: dict):
    key = input("\nPlease insert the key of a translation you wish to remove: ")
    if key not in dict:
        print(f"Key '{key}' is not existing in dictionary.")
        return
    removed_value = dict.pop(key)
    print(f"Removed entry: {key} -> {removed_value}.")

dict = {"ja": "yes", "nein": "no"}
MODES = {"s": "show all", "t": "translate", "a": "add translation", "u": "update", "r": "remove", "x": "exit"}

mode = None
while mode != "x":
    print(SEPARATOR)
    mode = get_mode(MODES)
    match mode:
        case "s":
            print_dictionary(dict)
        case "t":
            translate(dict)
        case "a":
            add_entry_to_dictionary(dict)
        case "u":
            update_entry_in_dictionary(dict)
        case "r":
            remove_entry_from_dictionary(dict)
        case "x":
            print("Exiting translator.")
        case _:
            print(f"Mode '{mode}' not existing.")
