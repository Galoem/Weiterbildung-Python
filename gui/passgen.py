import random
import string

def pwgenPro2(length_lower: int, length_upper: int, length_numbers: int, length_specials: int) -> str:
    pw = []
    pw += random.choices(string.ascii_lowercase, k=length_lower)
    pw += random.choices(string.ascii_uppercase, k=length_upper)
    pw += random.choices(string.digits, k=length_numbers)
    pw += random.choices(string.punctuation, k=length_specials)
    random.shuffle(pw)
    return "".join(pw)