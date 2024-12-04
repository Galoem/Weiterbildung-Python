import csv
from pprint import pprint

# data = []

# with open('Erwerbstaetige.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")

#     for line in csv_reader:
#         values = []
#         for element in line:
#             no_white_spaces = element.replace(" ", "")
#             if no_white_spaces.isnumeric():
#                 values.append(int(no_white_spaces))
#             else:
#                 values.append(element)
#         data.append(values)

# header = data.pop(0)

# # print(header)
# # pprint(data)

# dict_data = []
# for number in data:
#     dict_data.append(dict(zip(header, number)))

# pprint(dict_data)

my_dict = dict()
with open("Erwerbstaetige.csv", "r") as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, delimiter=";")

    for line in csv_dict_reader:
        my_dict.update({line["Jahr"]: line})
    
    for entry in my_dict.values():
        entry: dict
        entry.pop("Jahr")
        for (key, value) in entry.items():
            value: str
            value = value.replace(" ", "")
            int_value = int(value)
            entry.update({key: int_value})

pprint(my_dict)
