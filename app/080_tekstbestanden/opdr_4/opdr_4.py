# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:
# De vragen staan in een lijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Tekstbestand openen in 'append' modus zodat meerdere feestgangers worden toegevoegd
with open("feestgangers.txt", "a", encoding="utf-8") as f:

    # Dictionary om de resultaten op te slaan
    antwoorden = {}

    # Loop door alle vragen
    for i, vraag in enumerate(vragen, start=1):
        print(f"{i}. {vraag}")
        reactie = input()
        # Sla op in dictionary met duidelijke sleutel
        if i == 1:
            antwoorden["voornaam"] = reactie
        elif i == 2:
            antwoorden["achternaam"] = reactie
        elif i == 3:
            antwoorden["drank"] = reactie
        elif i == 4:
            antwoorden["eten"] = reactie

    # Bedankt‑bericht
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")

    # Wegschrijven naar tekstbestand
    f.write("----\n")
    f.write(f"voornaam: {antwoorden['voornaam']}\n")
    f.write(f"achternaam: {antwoorden['achternaam']}\n")
    f.write(f"drank: {antwoorden['drank']}\n")
    f.write(f"eten: {antwoorden['eten']}\n\n")

# Party enquete