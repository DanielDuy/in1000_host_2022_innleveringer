# Oppgave 1
class Motorsykkel:
    def __init__(self, merke, registreringsnummer):  # Konstruktør
        self.merke = merke  # Merke for motorsykkel
        self.registreringsnummer = registreringsnummer  # Registreringsnummer
        self.kilometerstand = 0  # Kilometeravstand

    # Opgave 2
    def kjor(self, km):  # Metode som legger til km i kilometerstand
        self.kilometerstand += km  # Legger til kilometerstand i objektet

    # Oppgave 3
    def hent_kilometerstand(self):  # Skal returnere kilometeravstanden
        return self.kilometerstand

    # Oppgave 6
    def skrivUt(self):  # Skriver ut alle intsansvariablene til objektet
        print(self.merke)
        print(self.registreringsnummer)
        print(self.kilometerstand)
