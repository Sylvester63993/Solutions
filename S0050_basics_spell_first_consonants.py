# Opgave 5: Forandre koden i funktionen spell_first_consonants() sådan at den gør hvad der står i dens dokumentation.

def spell_first_consonants(text, letter_limit):
    """
    Spells/prints the first letter_limit letters of text.
    Prints only consonants (a, e, i, o, u, y do not get printed).  """
    vowels = ["a", "e", "i", "o", "u", "y"]
    vowels_included = text[0:letter_limit]
    vowels_excluded = ""
    print(vowels_included)
    for letter in range(len(vowels_included)):
        if not vowels_included[letter] in vowels:
            vowels_excluded += vowels_included[letter]
    print(vowels_excluded)
    return vowels_excluded
spell_first_consonants("Hello world", 7)  # should print "Hll w"