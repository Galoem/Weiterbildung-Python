

def house_planner(front_doors: int, windows: int, rooms: int, has_basement: bool):
    print(f"""
Das zu bauende Haus hat:
    - {front_doors} Haustür(en)
    - {windows} Fenster
    - {rooms} Räume
    - und hat {"einen" if has_basement else "keinen"} Keller
""")

house_planner(3, 8, 10, False)
house_planner(front_doors=1, windows=7, rooms=5, has_basement=True)

