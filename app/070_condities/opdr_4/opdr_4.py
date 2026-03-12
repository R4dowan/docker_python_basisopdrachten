# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ...

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]

# Maak een lijst met alleen de namen
beschikbare_toppings = [t[0] for t in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze voorkomt in de lijst
gevonden = False
for naam, prijs in toppings:
    if keuze == naam:
        print(f"U heeft {naam} besteld. Dat kost {prijs}")
        gevonden = True
        break

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")

# Hier de rest van jouw code...