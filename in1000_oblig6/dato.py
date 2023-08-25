class Dato:  # Oppgave 1
    def __init__(self, ny_dag, ny_maaned, nytt_aar): # Konstruktør
        self.dag = ny_dag
        self.maaned = ny_maaned
        self.aar = nytt_aar

    # Oppgave 3
    # a.
    def hent_aar(self):  # Returnerer året for datoen
        return self.aar

    # b.
    def skrivUtIStreng(self):  # Skriver ut datoen i en streng
        return str(self.dag) + ' ' + str(self.maaned) + ' ' + str(self.aar)

    # c.
    def sjekkDagFinnes(self):  # Sjekker om dag finnes, returnerer True eller fales
        if self.dag > 0:
            return True
        else:
            return False
