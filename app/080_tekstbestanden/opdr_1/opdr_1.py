# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
# De drie vragen
vraag1 = input("Wat vind je van de huidige regering?\n")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")

# Schrijf de antwoorden weg in een tekstbestand
with open("enquete.txt", "w", encoding="utf-8") as f:
    f.write("Resultaten enquete:\n")
    f.write(f"1. Huidige regering: {vraag1}\n")
    f.write(f"2. Python-lessen: {vraag2}\n")
    f.write(f"3. Mooiste stad: {vraag3}\n")

print("De resultaten zijn opgeslagen in enquete.txt")