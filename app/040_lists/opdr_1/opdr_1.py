# Lege list aanmaken
personen = []

# Vier dictionaries met gegevens
persoon1 = {"id": 0, "voornaam": "Ali", "achternaam": "Karimi"}
persoon2 = {"id": 1, "voornaam": "Sara", "achternaam": "Jansen"}
persoon3 = {"id": 2, "voornaam": "Youssef", "achternaam": "El Amrani"}
persoon4 = {"id": 3, "voornaam": "Lina", "achternaam": "Bakker"}

# Dictionaries toevoegen aan de list (met list-methode append)
personen.append(persoon1)
personen.append(persoon2)
personen.append(persoon3)
personen.append(persoon4)

# Print de volledige naam van de 2e persoon in de list
tweede_persoon = personen[1]  # index 1 = 2e persoon
volledige_naam = tweede_persoon["voornaam"] + " " + tweede_persoon["achternaam"]

print("De volledige naam van de 2e persoon is:", volledige_naam)