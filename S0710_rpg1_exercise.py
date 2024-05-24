"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random


class Character:
    def __init__(self, name, max_health, _current_health, attackpower):
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower
        self.dmg_unit = "dmg"

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}'

    def get_hit(self, attackpower):
        if self._current_health <= 0:
            print("Cannot attack", self.name, "because character already is dead")
        else:
            self._current_health -= attackpower

    def get_hit2(self, other):
        if self._current_health <= 0:
            print("Cannot attack", self.name, "because character already is dead")
        else:
            self._current_health -= other.attackpower

    def get_healed(self):
        self._current_health += self.healpower
        if self._current_health > self.max_health:
            self._current_health = self.max_health

    def get_fireballed(self, spellpower):
        if self._current_health <= 0:
            print("Cannot spellattack ", self.name, " because character already is dead")
        random.random()
        if random.random() > .7:
            self._current_health -= spellpower * 2
            print("Critcal strike on ", self.name, " for 2x damage")
        else:
            self._current_health -= spellpower

    def get_multi_attacked(self, multi_attack_amount, attackpower):
        if self._current_health <= 0:
            print("Cannot multiattack ", self.name, " because character already is dead")
        minimum = 2
        maximum = 4
        multi_attack_amount = random.randint(minimum, maximum) *
    def hit(self, other):
        print(self.name, "giver", other.name, self.attackpower, self.dmg_unit)
        other.get_hit(self.attackpower)

    def hit2(self, other):
        print(self.name, "giver", other.name, self.attackpower, self.dmg_unit)
        other.get_hit2(self)


class Healer(Character):
    def __init__(self, name, max_health, _current_health, healpower):
        super().__init__(name, max_health, _current_health, attackpower=0)
        self.healpower = healpower
        self.hp_unit = "hp"

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}, Healpower: {self.healpower}'

    def heal(self, other):
        print(self.name, "giver", other.name, self.healpower, self.hp_unit)
        other.get_healed(self.healpower)


class Magician(Character):
    def __init__(self, name, max_health, _current_health, attackpower, max_mana_level, _current_mana_level, spellpower):
        super().__init__(name, max_health, _current_health, attackpower)
        self.max_mana_level = max_mana_level
        self._current_mana_level = _current_mana_level
        self.spellpower = spellpower

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}, Manalevel: {self.manalevel}'

    def throw_fireball(self, other, mana_cost=20):
        other.get_fireballed(self.spellpower)
        self._current_mana_level -= mana_cost


class Hunter(Character):
    def __init__(self, name, max_health, _current_health, attackpower, max_fatigue, _current_fatigue, multi_attack_amount):
        super().__init__(name, max_health, _current_health, attackpower)
        self.max_fatigue = max_fatigue
        self._current_fatigue = _current_fatigue
        self.multi_attack_amount = multi_attack_amount

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}, Manalevel: {self.manalevel}'

    def multi_attack(self, other, fatigue_increment):
        minimum = 2
        maximum = 4
        for i in range(random.randint(minimum, maximum)):
            other.get_hit(self.attackpower)
        self.

def main():
    char1 = Character('Warrior', 150, 100, 15)
    char2 = Character('Mage', 125, 100, 20)
    healer1 = Healer("Priest", max_health=100, _current_health=100, healpower=25)

    print(char1)
    print(char2)
    print(healer1)

    char1.hit(char2)
    print(char2)

    healer1.heal(char2)
    print(char2)


main()
