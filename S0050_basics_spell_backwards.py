# Opgave 4: Forandre koden i funktionen spell_backwards() sådan at den gør hvad der står i dens dokumentation.

def spell(text):
    for letter in text:
        print(letter, end="")
    print()


def spell_backwards(text):
    """Spells/prints text backwards"""
    for letter in range(len(text) - 1, -1, -1):
        print(text[letter], end="")
    print()


spell("Test")
spell_backwards("Hello world")  # should print "dlrow olleH"