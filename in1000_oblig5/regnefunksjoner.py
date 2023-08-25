# Programmet teste funksjoner som gjør regne oppgaver
# Oppgave 1
def addisjon(a, b):  # Definerer funksjon, med to argumenter
    summen = a + b  # Summerer to argumentene
    return summen  # Returnerer summen


print(addisjon(2, 5))  # Kjører funksjonen addisjon(a, b) og printer ut det funksjonen returnerer

# Oppgave 2
assert 5 == addisjon(3, 2)  # Tester funksjon addisjon(a, b), 3 + 2
assert -5 == addisjon(-3, -2)  # Tester funksjon addisjon(a, b), -3 + -2
assert 1 == addisjon(3, -2)  # Tester funksjon addisjon(a, b), 3 + -2


def subtraksjon(a, b):  # Definerer funksjon, med to argumenter
    summen = a - b  # Subtraherer den andre argumentet med det første og lagrer summen i en variabel
    return summen  # Returnerer summen


assert 2 == subtraksjon(4, 2)  # Tester funksjonen subtraksjon(a, b), 4 - 2
assert -2 == subtraksjon(-4, -2)  # Tester funksjonen subtraksjon(a, b), -4 - -2
assert 6 == subtraksjon(4, -2)  # Tester funksjonen subtraksjon(a, b), 4 - -2


def divisjon(a, b):  # Definerer en funksjon, med to argumenter
    summen = a / b  # Divderer første argument med andre argument, lagrer summen i en variabel
    return summen  # Returnerer summen


assert divisjon(6, 3)  # Tester funksjonen divisjon(a, b), med argumentene 6 og 3
assert divisjon(-6, -3)  # Tester funksjonen divisjon(a, b), med argumentene -6 og -3
assert divisjon(6, -3)  # Tester funksjonen divisjon(a, b), med argumentene 6 og -3


# Oppgave 3
def tommerTilCm(antallTommer):  # Definerer en funksjon med et argument
    assert antallTommer > 0  # Tester om argumentet, når funksjonen blir kalt, er en verdi større enn 0
    cm = antallTommer * 2.54  # Regner fra tommmer til centimeter og lagrer det i en variabel
    return cm  # Returnerer variabelen


assert tommerTilCm(24) == 60.96  # Kaller på funksjonen tommerTilCm(antallTommer) med argument 24. Tester funksjonen
# via "assert" om funksjonen beregner riktig


# Oppgave 4a
def skrivBeregninger():  # Definerer funksjonen skrivBeregninger()
    input1 = int(input("Skriv inn tall 1: "))  # Ber bruker skrive input og lagrer input i en variabel
    input2 = int(input("Skriv inn tall 2: "))  # Ber bruker skrive input og lagrer input i en variabel

    # Kaller på addisjon(a, b) med argumenter input1 og input2, og printer ut i en passende melding
    print("\nResultat av summering: {:.1f}".format(addisjon(input1, input2)))

    # Kaller på subtraksjon(a, b) med argumenter input1 og input2, og printer ut i en passende melding
    print("Resultat av subtraksjon: {:.1f}".format(subtraksjon(input1, input2)))

    # Kaller på divisjon(a, b) med argumenter input1 og input2, og printer ut i en passende melding
    print("Resultat av divisjon: {:.1f}".format(divisjon(input1, input2)))

    # Oppgave b
    print("\nKonvertering fra tommer til cm:")
    # Ber bruker skrive inn en input, gjør om input til typen int og lagrer den i en variabel
    input3 = int(input("Skriv inn et tall: "))
    # Kaller på tommerTilCm med argument input3 og printer ut i en passende melding
    print("Resultat: {:.2f}".format(tommerTilCm(input3)))


# Oppgave 5
skrivBeregninger()  # Tester/kjører funksjonen
