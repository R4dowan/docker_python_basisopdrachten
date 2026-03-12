# Dictionary met rivieren en landen waar ze doorheen stromen
rivier_info = {
    "rijn": ["nederland", "duitsland", "frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

# Maak een list met alleen de riviernamen
rivieren = list(rivier_info.keys())

# ---------------------------
# 1e rivier (index 0)
# ---------------------------
rivier1 = rivieren[0].capitalize()             # riviernaam
land1 = rivier_info[rivieren[0]][1].capitalize()  # 2e land (index 1)

print("De rivier", rivier1, "stroomt onder andere door", land1)


# ---------------------------
# 2e rivier (index 1)
# ---------------------------
rivier2 = rivieren[1].capitalize()
land2 = rivier_info[rivieren[1]][0].capitalize()  # 1e land (index 0)

print("\nDe rivier", rivier2, "stroomt onder andere door", land2)


# ---------------------------
# 3e rivier (index 2)
# ---------------------------
rivier3 = rivieren[2].capitalize()
land3 = rivier_info[rivieren[2]][2].capitalize()   # 3e land (index 2)

print("\nDe rivier", rivier3, "stroomt onder andere door", land3)