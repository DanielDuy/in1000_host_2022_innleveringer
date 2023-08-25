from motorsykkel import *  # Oppgave 4, importerer klassen


def hovedprogram():  # Oppretter funksjon hovdprogram()
    # Oppgave 6
    m1 = Motorsykkel('Honda', 'AD78045')  # Lager objekt fra klasse
    m2 = Motorsykkel('Yamaha', 'CF93021')  # Lager objekt fra klasse

    m1.skrivUt()  # Skriver ut objektet
    m2.skrivUt()  # Skriver ut objektet

    # Oppgave 7
    m2.kjor(10)  # Legger til 10 km i kilometerstand for m2

    print(m2.hent_kilometerstand())  # Printer ut nye kilometerstand fro m2


# Oppgave 8
hovedprogram()  # Kaller på funksjonen
