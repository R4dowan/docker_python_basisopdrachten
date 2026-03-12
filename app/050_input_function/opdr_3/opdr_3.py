# Maak een lege lijst aan
steden = []

# Vraag de gebruiker om minimaal 5 steden in te vullen
print("Vul minimaal 5 steden in:")

for i in range(5):
    stad = input(f"Geef stad {i+1}: ")
    steden.append(stad)

# Sorteer de lijst in omgekeerde (reverse) alfabetische volgorde
steden.sort(reverse=True)

# Items die beginnen met Z moeten vooraan komen
z_steden = [s for s in steden if s.lower().startswith("z")]
overige_steden = [s for s in steden if not s.lower().startswith("z")]

# Combineer zodat Z-items vooraan staan
gesorteerd = z_steden + overige_steden

# Print de uiteindelijke lijst
print(gesorteerd)