# první příklad – porovnání čísel

cislo_1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))

if cislo_1 == cislo_2:
    print("Čísla jsou si rovna.")
elif cislo_1 > cislo_2:
    print("První číslo je větší.")
else:
    print("První číslo je menší.")


# druhý příklad - string – je celý velkými písmeny?

text = input("Zadej text: ")

if text.isupper():
    print("Text je celý velkými písmeny.")
else:
    print("Text není celý velkými písmeny.")
