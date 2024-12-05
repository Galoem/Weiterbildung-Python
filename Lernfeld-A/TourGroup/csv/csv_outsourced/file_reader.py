import csv

def is_float(input: str) -> bool:
    try:
        float(input)
        return True
    except:
        print(f"value could not be formatted '{input}'")
        return False

def pop_empty_keys_and_year(entry: dict) -> None:
    entry.pop("Jahr")
    if "" in entry.keys():
        entry.pop("")

def build_inner_dict(result_dict: dict) -> None:
    for entry in result_dict.values():
        entry: dict
        pop_empty_keys_and_year(entry)
        for (key, value) in entry.items():
            value: str
            value_no_whitespaces = value.replace(" ", "").replace(",", ".")
            if is_float(value_no_whitespaces):
                numeric_value = float(value_no_whitespaces)
                entry.update({key: numeric_value})

def read_csv_dict(file_name: str, delimiter: str) -> dict:
    result_dict = dict()
    with open(file_name, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
        for line in csv_reader:
            result_dict.update({line["Jahr"]: line})
        build_inner_dict(result_dict)
    return result_dict
