from pprint import pprint
import sqlite3 as sqlite
import csv_reader

ERWERBSTAETIGE_CSV_PATH = "../source_data/Erwerbstaetige.csv"
KONSUMENTWICKLUNG_CSV_PATH = "../source_data/Konsumentwicklung.csv"
LOHNENTWICKLUNG_CSV_PATH = "../source_data/Lohnentwicklung.csv"
NEXT_LINE_INDENTED = ",\n    "

def create_table(cursor: sqlite.Cursor, table_name: str, data: dict) -> None:
    header = get_header_names(data)
    init_str = build_create_table_str(table_name, header)
    cursor.execute(init_str)

def build_create_table_str(table_name, header):
    header_init_str = ""
    for header_name in header:
        header_init_str += (f"{header_name.replace("-", "_").replace(" ", "_")} REAL" + NEXT_LINE_INDENTED)
    
    header_init_str = header_init_str.removesuffix(NEXT_LINE_INDENTED)

    init_str = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Jahr INTEGER,
    {header_init_str}
)"""

    return init_str

def get_header_names(data):
    header = list()

    values: dict = data.popitem()
    for key in values[1].keys():
        header.append((key))
    return header

def insert_values(cursor: sqlite.Cursor, table_name: str, data: dict) -> None:
    headers = list()
    values = list()

    pprint(data)
    headers.append("Jahr")
    
    value_init_str = f"""
INSERT INTO {table_name} ({headers}) VALUES   
    ('data1', 'data2'),
    ('data1', 'data2'),
    ('data1', 'data2'),
    ('data1', 'data2');
"""


    # cursor.executemany(f"INSERT INTO {table_name} ({headers}) VALUES ({values})")

erwerbstaetige_data: dict = csv_reader.read_csv_dict(ERWERBSTAETIGE_CSV_PATH, ";")
konsumentwicklung_data: dict = csv_reader.read_csv_dict(KONSUMENTWICKLUNG_CSV_PATH, ";")
lohnentwicklung_data: dict = csv_reader.read_csv_dict(LOHNENTWICKLUNG_CSV_PATH, ";")

connection: sqlite.Connection = sqlite.connect("stats.db")
cursor:sqlite.Cursor = connection.cursor()

create_table(cursor, "erwerbstaetige", erwerbstaetige_data)
create_table(cursor, "konsumentwicklung", konsumentwicklung_data)
create_table(cursor, "lohnentwicklung", lohnentwicklung_data)

insert_values(cursor, "erwerbstaetige", erwerbstaetige_data)
insert_values(cursor, "konsumentwicklung", konsumentwicklung_data)
insert_values(cursor, "lohnentwicklung", lohnentwicklung_data)
