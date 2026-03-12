resultaat = []

# range van 3 t/m 81, met stappen van 3
for n in range(3, 82, 3):
    # n in het kwadraat en daarna delen door 3
    waarde = (n ** 2) / 3
    resultaat.append(waarde)

print(resultaat)