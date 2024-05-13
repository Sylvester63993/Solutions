"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen motorlyd

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne S0420_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du stadig er gået i stå, skal du åbne S0430_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Team-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

def drive_car():
    print("Vrooom!")  # print a sound


car1_wheels = 4  # define number of wheels for car1
car1_max_speed = 100  # define maximum speed for car1
car2_wheels = 6  # define number of wheels for car2
car2_max_speed = 120  # define maximum speed for car2

print("Number of wheels:", car1_wheels, "Max speed:", car1_max_speed, "km/h")  # print out the properties of car1
print("Number of wheels:", car2_wheels, "Max speed:", car2_max_speed, "km/h")  # print out the properties of car2

drive_car()  # call drive_car
