# Maak een lijst met gasten
gasten = []

# Voeg jezelf toe via input
jij = input("Vul je eigen naam in: ")
gasten.append(jij)

# Voeg de standaard personen toe
gasten.extend(["Paul", "Kees", "Marie", "Hilda"])

# Print de beginlijst
print(gasten)

# Marie gaat niet mee → verwijder haar
gasten.remove("Marie")

# Print de lijst zonder Marie
print(gasten)

# George gaat wel mee → hij moet naast Kees zitten
index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")

# Print de definitieve lijst
print(gasten)
