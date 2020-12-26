set_boje = {"Plava", "Zelena", "Crna", "Zuta"}

print(set_boje)

set_voce = (("Jagode", "Breskve", "Sljive"))
print(type(set_voce))

ulaz = input("Sta ti treba?: ")

if ulaz in set_boje:
    print("Postoji")
