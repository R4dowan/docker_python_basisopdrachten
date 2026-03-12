# Opdracht 1 functies
# Naam student:
# Groep:


def kubus_vol(m):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

def bol_vol(r):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))
import math

def kubus_vol(zijde):
    # Volume kubus = zijde³
    return zijde ** 3


def bol_vol(straal):
    # Volume bol = 4/3 * π * straal³
    return (4/3) * math.pi * (straal ** 3)


# Voorbeelden zoals in opdracht:
kubus = kubus_vol(5)
print(f"De inhoud van deze kubus is: {kubus}")

bol = bol_vol(4)
print(f"De inhoud van deze bol is: {bol}")