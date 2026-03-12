# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

def miles_naar_kilometers(miles):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

kilometers = 1223
miles = 867

print(kilometers_naar_miles(kilometers))
print(miles_naar_kilometers(miles))

def kilometers_naar_miles(km):
    return km / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344


# Voorbeeldwaarden
kilometers = 1223
miles = 867

# Functie-aanroepen
miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

# Output
print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")
