class Hund:  # Oppave 1
    def __init__(self, alder, vekt):  # Konstruktør
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10  # Instansverdi

    # Oppgave 3
    def hent_alder(self):  # Returnerer alderen til objektet
        return self.vekt

    def hent_vekt(self): # Returnerer vekten til objektet
        return  self.alder

    # Oppgave 4
    def spring(self):  # Minker metthet og vekt dersom metthet er under 5
        self.metthet -= 1
        if self.metthet < 5:
            self.vekt -= 1

    # Oppgave 5
    def spis(self, heltall):  # Legger til metthet og mett dersom metthet er over 7
        self.metthet += heltall
        if self.metthet > 7:
            self.vekt += 1
