
from pprint import pprint
class Pencil:
    count_pencil = 0
    def __init__(self, mine_length: int = 12):
        Pencil.count_pencil += 1
        self.manufacturer = "Faber-Castell"
        self.model = "Grip 2001"
        self.mine_length_original = mine_length
        self.mine_length_current = self.mine_length_original
        self.is_sharp = True

    def __str__(self): # Lesbarer Abruf, z.B. über print()
        result = f"{self.__class__.__name__}: " + "{"
        for attribute, value in self.__dict__.items():
            result += f"{attribute}:{value}, "
        return result.removesuffix(", ") + "}"

    def __repr__(self): # Technischer/struktureller Abruf, z.B. pprint()
        return f"{self.__class__.__name__}()"

    def write_norm_page(self):
        MIN_LENGTH = 5
        if self.mine_length_current < MIN_LENGTH:
            print(f"ERROR: Current mine length insufficient (must be at least {MIN_LENGTH}): {self.mine_length_current}")
            return
        self.mine_length_current -= 5
        self.is_sharp = False

    def sharpen_pencil(self):
        MIN_LENGTH = 2
        if self.mine_length_current < MIN_LENGTH:
            print(f"ERROR: Current mine length insufficient (must be at least {MIN_LENGTH}): {self.mine_length_current}")
            return
        self.mine_length_current -= 1
        self.is_sharp = True
    
    def merge_pencils(self, other: "Pencil"):
        merged_pencil = Pencil(self.mine_length_current + other.mine_length_current)
        merged_pencil.is_sharp = self.is_sharp
        merged_pencil.mine_length_original = self.mine_length_original + other.mine_length_original
        return merged_pencil

my_pencil = Pencil()
print(my_pencil)
pprint(my_pencil)

my_pencil.write_norm_page()
print(my_pencil)

my_pencil.write_norm_page()
print(my_pencil)

my_pencil.write_norm_page()
print(my_pencil)

my_pencil.sharpen_pencil()
print(my_pencil)

my_pencil.sharpen_pencil()
print(my_pencil)

my_used_pencil = Pencil(4)
print(my_used_pencil)

my_merged_pencil = my_pencil.merge_pencils(my_used_pencil)
print(my_merged_pencil)
