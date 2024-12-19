boolean_map = {"ja": True, "nein": False}

print("Beginn")
if boolean_map.get(input("Funktioniert die Anlage? ")):
    print("Fummel bloß nicht dran rum!")
    print("Pfeife unauffällig \"La paloma\" und verschwinde!")
    print("Alles klar!")
else:
    if boolean_map.get(input("Hast du daran herumgespielt? ")):
        print("Du Rindvieh!")
        if boolean_map.get(input("Hat es jemand gemerkt? ")):
            print("Du armes Schwein!")
            if boolean_map.get(input("Kannst du jemandem die Schuld zuschieben? ")):
                print("Alles klar!")
            else:
                print("Du armes Schwein!")
        else:
            print("Pfeife unauffällig \"La paloma\" und verschwinde!")
            print("Alles klar!")
    else:
        if boolean_map.get(input("Wird man dich dafür verantwortlich machen? ")):
            print("Du armes Schwein!")
            if boolean_map.get(input("Kannst du jemandem die Schuld zuschieben? ")):
                print("Alles klar!")
            else:
                print("Du armes Schwein!")
        else:
            print("Kümmer' dich nicht drum!")
            print("Alles klar!")