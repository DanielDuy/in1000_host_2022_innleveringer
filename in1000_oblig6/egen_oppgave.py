"""
Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
instansvariabel hobbyer som en tom liste . Skriv en metode leggTilHobby som tar
imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
alder kaller på metoden skrivHobbyer.
Lag deretter et testprogram for klassen Person der du lar brukeren skrive inn navn og
alder, og oppretter et Person-objekt med informasjonen du får. Deretter skal brukeren
ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger
ønsker å oppgi hobbyer skal informasjon om brukeren skrives ut.
"""


class Person:  # Oppgave 1
    def __init__(self, navn, alder):  # Kontruktør
        self.navn = navn
        self.alder = alder
        self.hobbyer = []

    def leggTilHobby(self, ny_hobby):  # Legger til hobby i listen med argument
        self.hobbyer.append(ny_hobby)

    def skrivHobbyer(self):  # Skriver ut alle hobbyene
        for hobby in self.hobbyer:
            print(hobby)

    def skrivUt(self):  # Skriver ut navnet, alderen og kaller på metoden skrivHobbyer()
        print(self.navn)
        print(self.alder)
        self.skrivHobbyer()
