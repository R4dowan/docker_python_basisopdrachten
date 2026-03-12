# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

getallen = []

# Vul de lijst met getallen 1 t/m 10
for i in range(1, 11):
    getallen.append(i)

# Print alleen de getallen groter dan 4
resultaat = []
for g in getallen:
    if g > 4:
        resultaat.append(g)

print(resultaat)

#for loop
#if statement