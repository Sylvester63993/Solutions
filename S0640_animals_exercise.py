"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en klassemetode ved navn wag_tail for Dog.
    Denne metode udskriver i konsollen noget i stil med
    "Hunden Snoopy vifter med sin 32 cm lange hale"
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google hvordan man laver det.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


import random

class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f'name: {self.name}, sound: {self.sound}, height: {self.height}, weight: {self.weight}, legs: {self.legs}, female: {self.female}'

    def make_noise(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.tail_length_unit = "cm"
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return f'name: {self.name}, sound: {self.sound}, height: {self.height}, weight: {self.weight} kg, legs: {self.legs}, female: {self.female}, tail_length: {self.tail_length} {self.tail_length_unit}, hunts_sheep: {self.hunts_sheep}'

    def __add__(self, other):
        return self.mate(other)

    def wag_tail(self):
        print(f'Hunden {self.name} logrer med sin {self.tail_length} {self.tail_length_unit} lange hale')

    def mate(self, other):
        if self.female != other.female:
            random_number = random.random()
            if random_number > 0.5:
                puppy_female = True
            else:
                puppy_female = False
            # puppy_female = random_number > 0.5 # kortere version

            puppy_gender = other.female
            if puppy_gender:
                puppy_sound = "Vuuvuvuvuv!"
                puppy_height = ((other.height+self.height) / 2) * 0.8
                puppy_weight = ((other.weight+self.weight) / 2) * 0.9
                puppy_tail_length = ((other.tail_length+self.tail_length) / 2) * 0.95
            else:
                puppy_sound = "Vovovovoov!"
                puppy_height = ((other.height+self.height) / 2) * 1.2
                puppy_weight = ((other.weight+self.weight) / 2) * 1.1
                puppy_tail_length = ((other.tail_length+self.tail_length) / 2) * 1.05

            random_number = random.random()
            puppy_hunts_sheep = random_number > 0.5

            maximum = 4
            minimum = 3
            for i in range(5):
                puppy_legs = random.randint(minimum, maximum)
            # puppy_sound = "aaa" if puppy_gender else "bbb" # Kortere version af den for oven
            puppy = Dog('Puppy', sound=puppy_sound, height=puppy_height, weight=puppy_weight, legs=puppy_legs, female=puppy_female, tail_length=puppy_tail_length, hunts_sheep=puppy_hunts_sheep)
            print(puppy.sound)
            # print(puppy.legs)
            return puppy


def main():
    animal = Animal('Ko', sound='Muuuh!', height=140, weight=700, legs=4, female=True)
    animal.make_noise()

    dog = Dog('Snoopy', sound='Vov!', height=15, weight=36, legs=4, female=False, tail_length=15, hunts_sheep=True)
    dog.wag_tail()

    dog2 = Dog('Snoopette', sound='Vuf!', height=12, weight=32, legs=4, female=True, tail_length=12, hunts_sheep=True)
    new_dog = dog2.mate(dog)
    new_dog2 = dog+dog2
    print(animal)
    print(new_dog)
    print(new_dog2)
    print(dog)
    print(dog2)


main()
