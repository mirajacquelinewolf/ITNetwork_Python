vstup = " C++ je [kolikrat] KRÁT lepší! "

vstup = vstup.strip()
vstup = vstup.lower()
vstup = vstup.replace("c++", "python")

if "python" in vstup and "krát" in vstup:
    pocet_znaku = len(vstup) * 3
    vstup = vstup.replace("[kolikrat]", str(pocet_znaku))
    print(vstup)
else:
    print("Věta neobsahuje Python a slovo krát.")