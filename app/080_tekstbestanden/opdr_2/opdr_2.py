# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
import random

geheim = random.randint(1, 100)
pogingen = 0

while True:
    gok = int(input("Raad mijn geheime getal\n"))
    pogingen += 1

    if gok < geheim:
        print("hoger")
    elif gok > geheim:
        print("lager")
    else:
        print(f"Je hebt het getal geraden! Het is {geheim}!")
        print(f"Je hebt het in {pogingen} keer gedaan")
        break

# De rest moet jij doen.....

