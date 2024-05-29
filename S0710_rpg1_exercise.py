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

    def get_healed(self, healpower):
        self._current_health += healpower
        if self._current_health > self.max_health:
            self._current_health = self.max_health

    def get_fireballed(self, spellpower):
        if self._current_health <= 0:
            print("Cannot spellattack ", self.name, " because character already is dead")
        random.random()
        if random.random() > .7:
            self._current_health -= spellpower * 2
            print ("Critical strike on", self.name, "for", (spellpower * 2), "damage (2x damage)")
        else:
            self._current_health -= spellpower
            print("Someone hit with a fireball for", spellpower, "damage")

    def get_fireballed2(self, other):
        if self._current_health <= 0:
            print("Cannot spellattack ", self.name, " because character already is dead")
        random.random()
        if random.random() > .7:
            self._current_health -= other.spellpower * 2
            print(other.name, "has hit a critical strike on", self.name, "for", (other.spellpower * 2), "damage (2x damage)")
        else:
            self._current_health -= other.spellpower
            print(other.name, "has hit", self.name, " with a fireball for", other.spellpower, "damage")

    def regenerate_health(self):
        self._current_health += 10
        if self._current_health > self.max_health:
            self._current_health = self.max_health

    def regenerate_mana(self):
        pass

    def decrease_fatigue(self):
        pass

    def regenerate(self):
        self.regenerate_mana()
        self.regenerate_health()
        self.decrease_fatigue()

    def hit(self, other):
        print(self.name, "giver", other.name, self.attackpower, self.dmg_unit)
        other.get_hit(self.attackpower)

    def hit2(self, other):
        print(self.name, "gives", other.name, self.attackpower, self.dmg_unit)
        other.get_hit2(self)

    def dead(self):
        return self._current_health <= 0 #True hvis død

class Healer(Character):
    def __init__(self, name, max_health, _current_health, healpower):
        super().__init__(name, max_health, _current_health, attackpower=0)
        self.healpower = healpower
        self.hp_unit = "hp"

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}, Healpower: {self.healpower}'

    def heal(self, other):
        print(self.name, "heals", other.name, self.healpower, self.hp_unit)
        other.get_healed(self.healpower)


class Magician(Character):
    def __init__(self, name, max_health, _current_health, attackpower, max_mana_level, _current_mana_level, spellpower):
        super().__init__(name, max_health, _current_health, attackpower)
        self.max_mana_level = max_mana_level
        self._current_mana_level = _current_mana_level
        self.spellpower = spellpower

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}, Mana level: {self._current_mana_level}'

    def throw_fireball(self, other, mana_cost=20):
        if self._current_mana_level < mana_cost:
            print(self.name, "doesn't have enough mana to throw fireball at", other.name)
        else:
            self._current_mana_level -= mana_cost
            # other.get_fireballed(self.spellpower)
            other.get_fireballed2(self)
            print(self.name, "throws fireball at", other.name, "for", self.spellpower, "damage")

    def regenerate_mana(self):
        self._current_mana_level += 10
        if self._current_mana_level > self.max_mana_level:
            self._current_mana_level = self.max_mana_level


class Hunter(Character):
    def __init__(self, name, max_health, _current_health, attackpower, max_fatigue, _current_fatigue):
        super().__init__(name, max_health, _current_health, attackpower)
        self.max_fatigue = max_fatigue
        self._current_fatigue = _current_fatigue

    def __repr__(self):
        return f'name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attackpower: {self.attackpower}, Fatigue level: {self._current_fatigue}'

    def multi_attack(self, other, fatigue_increment=30):
        # self._current_fatigue += fatigue_increment
        if self._current_fatigue >= self.max_fatigue:
            self._current_fatigue = self.max_fatigue
            print(self.name, "cannot multiattack ", other.name, " because fatigue level is too high")
        else:
            minimum = 2
            maximum = 4
            for i in range(random.randint(minimum, maximum)):
                other.get_hit(self.attackpower)
                print(self.name, "multiattacks ", other.name, "for ", self.attackpower, "damage")
        self._current_fatigue += fatigue_increment

    def decrease_fatigue(self):
        self._current_fatigue -= 20
        if self._current_fatigue < 0:
            self._current_fatigue = 0

def main():
    char1 = Character('Warrior', 100, 100, 15)
    char2 = Character('Warlock', 100, 100, 20)
    healer1 = Healer("Priest", max_health=100, _current_health=100, healpower=25)
    magician1 = Magician("Magician", max_health=100, _current_health=100, attackpower=10, max_mana_level=100, _current_mana_level=100, spellpower=20)
    hunter1 = Hunter("Hunter", max_health=100, _current_health=100, attackpower=25,_current_fatigue=0, max_fatigue=100)

    # print(char1)
    # print(char2)
    # print(healer1)
    print(magician1)
    print(hunter1)

    # char1.hit(char2)
    # print(char2)

    # healer1.heal(char2)
    # print(char2)

    # hunter1.multi_attack(magician1)
    # hunter1.multi_attack(magician1)
    # print(magician1)
    # magician1.regenerate()
    # print(magician1)
    # print(hunter1)
    # magician1.throw_fireball(hunter1)
    # print(hunter1)

    print(magician1, hunter1)
    for i in range(2):
        while not hunter1.dead() and not magician1.dead():
            magician1.throw_fireball(hunter1)
            print(hunter1)
        else:
            hunter1.multi_attack(magician1)
            print(magician1)

main()
