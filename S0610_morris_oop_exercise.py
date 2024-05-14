"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:
    def __init__(self, sleepiness, thirst, hunger, whisky, gold, turn):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold
        self.turn = turn

    def __repr__(self):
        return f"Morris Attributes - Turn Number: {self.turn} Gold: {self.gold} Hunger: {self.hunger} Thrist: {self.thirst} Whisky: {self.whisky} Sleepiness: {self.sleepiness}"

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def drink(self):
        if self.whisky > 0:
            self.whisky -= 1
            self.sleepiness += 5
            self.thirst -= 15

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        if self.whisky < 10:
            self.whisky += 1
            self.sleepiness += 5
            self.hunger += 1
            self.gold -= 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.gold += 5

    def dead(self):
        if self.sleepiness > 100 or self.hunger > 100 or self.thirst > 100:
            print("Morris has died")
            return True
        else:
            return False


def main():
    morris = Miner(0, 0, 0, 0, 0, 0)

    while not morris.dead() and morris.turn < 1000:
        morris.turn += 1
        # Choose the activity that maximizes gold
        if morris.whisky < 1 and morris.gold >= 1:  # ChatGPT-værdi: < 10 >= 1
            morris.buy_whisky()
        elif morris.whisky > 0 and morris.thirst >= 96:  # ChatGPT-værdi: > 0 >= 15
            morris.drink()
        elif morris.hunger >= 99 and morris.gold >= 2:  # ChatGPT-værdi: >= 20 >= 2
            morris.eat()
        elif morris.sleepiness > 84:  # max gold værdi 84
            morris.sleep()
        else:
            morris.mine()

        print(morris)


main()
