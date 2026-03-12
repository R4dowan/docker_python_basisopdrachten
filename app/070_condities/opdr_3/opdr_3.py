# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

normale_toegangsprijs = 12.50
kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
leeftijdsgroepen = { "baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150) }

leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))

# Bepaal de juiste groep
groep = None
for naam, (min_leeftijd, max_leeftijd) in leeftijdsgroepen.items():
    if min_leeftijd <= leeftijd <= max_leeftijd:
        groep = naam
        break

# Haal percentage korting op
korting = kortings_percentages[groep]

# Bereken prijs
te_betalen = normale_toegangsprijs * (1 - korting / 100)

# Output
print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {te_betalen}")



# Hier komt je code...
