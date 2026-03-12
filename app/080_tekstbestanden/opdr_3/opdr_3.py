# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

tekst = input("Geef de tekst die wilt encrypten..\n")

versleuteld = ""

for char in tekst:
    # Check of het een letter is
    if char.isalpha():
        # Zet om naar kleine letters voor gemak
        basis = ord('a') if char.islower() else ord('A')
        
        # Letter verschuiven met 5 plaatsen
        nieuwe_code = (ord(char) - basis + 5) % 26 + basis
        
        versleuteld += chr(nieuwe_code)
    else:
        # Niet-letters blijven hetzelfde (spaties, komma’s, enz.)
        versleuteld += char

print(versleuteld)


