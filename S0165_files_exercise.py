"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum og et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

myfile = "S0165_input.txt" # the name of the file. Note the / (slash) instead of a \ (backslash) in the file path!

# Åbn filen i læsetilstand
with open(myfile, 'r') as file:
    # Læs alle linjer fra filen og gem dem i en liste
    lines = file.readlines()

# Gennemgå hver linje i listen
for line in lines:
    # Split linjen i navn og alder ved at bruge mellemrum som adskillelse
    parts = line.split()

    # Hvis linjen er tom, spring over til næste iteration
    if not parts:
        continue

    # Udpak navn og alder fra listen af dele
    name, age = parts[0], parts[1]

    # Udskriv resultatet
    print(f"{name} er {age} år gammel.")